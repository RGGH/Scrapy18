import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

class ebayspider(Spider):

    name = 'ebaypider'
    allowed_domains = ['ebay.co.uk']

    def __init__(self):
        self.link_extractor = LinkExtractor()

    with open('data.csv') as file:
        start_urls = [line.strip() for line in file]

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        yield request

    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            yield Request(link.url, callback=self.parse)


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(ebayspider)
    process.start()
