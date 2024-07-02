import scrapy
from urllib.parse import urljoin

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        # Your initial code here

        # Simplified URL construction
        next_page = response.css('li.next a ::attr(href)').get()
        if next_page:
            next_page_url = urljoin(response.url, next_page)
            yield response.follow(next_page_url, callback=self.parse)

    def parse_book_page(self, response):
        table_rows = response.css("table tr")
        book_item = BookItem()

        # Corrected assignments without trailing commas
        book_item['url'] = response.url
        book_item['upc'] = table_rows[0].css('td ::text').get()
        book_item['title'] = response.css('h1 ::text').get()
        book_item['price'] = response.css('.price_color ::text').get()
        # Your other field assignments here, corrected as needed

        yield book_item