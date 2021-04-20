import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess


class stackospider(Spider):
    name = 'stackospider'

    with open('data.csv') as file:
        start_urls = [line.strip() for line in file]

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        yield request

    def parse(self,response):
        pass

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(stackospider)
    process.start()
