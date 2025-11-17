import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
    }

    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=5)
            if response.status_code == 200:
                return response.text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
    return None

def parse_headlines(html):
    soup = BeautifulSoup(html, "html.parser")

    candidates = []
    tags = ["h1", "h2", "h3", "h4"]

    for tag in tags:
        for item in soup.find_all(tag):
            text = item.get_text(strip=True)
            if text and len(text) > 20:
                candidates.append(text)

    return list(dict.fromkeys(candidates))[:20]

def save_to_txt(headlines, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("Top News Headlines\n")
        f.write("Generated on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        f.write("-------------------------------------\n\n")

        for index, headline in enumerate(headlines, 1):
            f.write(f"{index}. {headline}\n")

def main():
    url = "https://www.bbc.com/news"

    print("Fetching headlines...")

    html = fetch_page(url)
    if not html:
        print("Error. Could not fetch webpage.")
        return

    headlines = parse_headlines(html)

    if not headlines:
        print("No headlines found.")
        return

    output_file = "headlines.txt"
    save_to_txt(headlines, output_file)

    print(f"\nDone. Headlines saved to {output_file}")

if __name__ == "__main__":
    main()
