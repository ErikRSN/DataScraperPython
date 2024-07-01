# BookHarvester: A Scrapy Book Scraper

Ths app uses Python Scrapy library to extract book details (title, price, rating, availability) from the "Books to Scrape" website and store the bookdata in the csv file.

## Installation

1. Clone the repository:

   - `git clone https://github.com/ErikRSN/DataScraperPython`
   - `cd BookHarvester`

2. Set up a virtual environment:

   - For Windows:
     - `python -m venv venv`
     - `venv\Scripts\activate`
   - For macOS/Linux:
     - `python3 -m venv venv`
     - `source venv/bin/activate`

3. Install dependencies:
   - `pip install -r requirements.txt`

## Usage

Run the scraper:

- `scrapy crawl bookscraper`

## Contributing

Fork the repository and submit a pull request.
