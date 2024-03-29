import requests
from bs4 import BeautifulSoup
import os
import sys

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Save page content to a .html file
    filename = os.path.join('scraped_pages', url.split('/')[-1] + '.html')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    # Find the link to the next page and return it
    next_link = soup.find('a', {'class': 'next'})
    if next_link:
        return next_link.get('href')

def main(url):
    next_page = scrape_page(url)

    while next_page:
        next_page = scrape_page(os.path.join(url, next_page))

if __name__ == "__main__":
    main(sys.argv[1])