import requests as req
from bs4 import BeautifulSoup as BS
import sys

def scraper(address):
    agent = {"User-Agent": "Mozilla/5.0"}

    page = req.get(address, headers=agent)
    page.raise_for_status()
        
    soup = BS(page.content, "html.parser")

    # Page Title
    if soup.title:
        print(soup.title.get_text().strip())
    else:
        print("Title not found!")

    # Page Body
    if soup.body:
        print(soup.body.get_text(separator="\n", strip=True))
    else:
        print("Body not found!")

    # All Links
    for links in soup.find_all("a"):
        url = links.get("href")
        if url:
            print(url)


def main():
    # URL from the command line, e.g. "python web_scraper.py https://www.siren.io"
    if len(sys.argv) != 2:
        print("Give CLP as: python web_scraper.py <URL>")
    else:
        url = sys.argv[1]
        scraper(url)


if __name__ == "__main__":
    main()
