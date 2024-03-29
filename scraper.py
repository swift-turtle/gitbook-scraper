import shutil
import sys
from pathlib import Path
from typing import List, Set
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup

ROOT_FOLDER = 'output'


def scrape_page(base_url: str, url: str, scraped_urls: Set[str]):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        route_items: List[str] = [i for i in urlparse(url).path.split('/') if i]

        if route_items:
            route_items[-1] = route_items[-1] + '.html'
            base_path = Path(ROOT_FOLDER) / urlparse(url).netloc
        else:
            base_path = Path(ROOT_FOLDER) / urlparse(url).netloc / 'index.html'

        file = base_path / '/'.join(route_items)
        file.parent.mkdir(parents=True, exist_ok=True)

        with open(file, 'w', encoding='utf-8') as f:
            f.write(str(soup))

        for href in set(href for nl in soup.find_all('a') if (href := nl.get('href')) and href.startswith('/')):
            url = urljoin(base_url, href)

            if url not in scraped_urls:
                scraped_urls.add(url)
                print(f'Scraping {url}')
                scrape_page(base_url, url, scraped_urls)
    except Exception as e:
        print(f'Error while scraping {url}: {e}')


def main(url):
    directory = Path(ROOT_FOLDER) / urlparse(url).netloc

    if directory.exists():
        shutil.rmtree(directory, ignore_errors=True)

    scrape_page(url, url, set())


if __name__ == "__main__":
    main(sys.argv[1])
    print('Done scraping!')
