# gitbook-scraper
A Gitbook Web Crawler & Scraper

# Goal
Automates the process of crawling a gitbook and scraping all the webpages.

# Pre-requisites
1. Install [Python](https://www.python.org/downloads/)
2. Install [Git](https://git-scm.com/downloads)

# Installation
```shell
git clone https://github.com/ghovander/gitbook-scraper.git
cd gitbook-scraper
pip install -r requirements.txt
```

# Usage
1. Run the scraper
   - Scrape from the root of the gitbook
       ```shell
       python scraper.py 'https://my-gitbook.com'
       ```
   - Scrape from a specific section
       ```shell
       python scraper.py 'https://my-gitbook.com/section'
       ```
2. View the output
    - The scraped webpages will be saved to the `output` directory.

