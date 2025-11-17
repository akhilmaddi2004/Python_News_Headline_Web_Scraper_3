## 📌 News Headlines Web Scraper (Python)

This project is a console-based Python web scraper that collects the latest news headlines from a public news website and saves them into a clean, well-formatted text file. It uses requests to fetch the webpage and BeautifulSoup to parse and extract headline tags.

## ⭐ Features

- Fetches latest news headlines from a live website
- Parses and extracts headline titles using BeautifulSoup
- Stores all collected headlines in a .txt file
- Automatically creates the output file if it doesn't exist
- Clean terminal output for quick verification
- Simple, fast and beginner-friendly script

## 🛠️ Technologies Used

- Python
- requests
- BeautifulSoup (bs4)

## ▶️ How to Run

1. Install required module:
- pip install requests beautifulsoup4

2.Run the script:
- python news_scraper.py

3.After running, check the file:
- headlines.txt

## 📁 Files Included

- news_scraper.py → Main scraping script
- headlines.txt → Auto-generated file containing saved headlines

## 📸 Screenshots
1. news_scraper.py Code
![Screenshot](https://github.com/akhilmaddi2004/Python_News_Headline_Web_Scraper_3/blob/main/News_scraper_3/news1.png)
3. Generated headlines.txt File
![Screenshot](https://github.com/akhilmaddi2004/Python_News_Headline_Web_Scraper_3/blob/main/News_scraper_3/news_txt.png )

## ✔️ Output Example (Terminal)

- Fetching headlines...
- 10 headlines extracted successfully.
- Saved to headlines.txt

## 📚 What This Project Demonstrates

- Basic HTTP GET request handling
- HTML parsing and tag selection
- Extracting structured data from a webpage
- File creation and safe text writing
- Intro-level automation for data collection
