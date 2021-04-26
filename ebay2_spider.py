# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

import os

class Ebayspider(Spider):

    name = 'ebayspider'
    allowed_domains = ['ebay.co.uk']
    start_urls = ['https://www.ebay.co.uk/deals']
    
    try:
        os.remove('ebay2.txt')
    except OSError:
        pass

    custom_settings = {
        'CONCURRENT_REQUESTS' : 2,               
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_DEBUG': True,
        'DOWNLOAD_DELAY': 1
    }

    def __init__(self):
        self.link_extractor = LinkExtractor(allow=\
            "https://www.ebay.co.uk/e/fashion/up-to-50-off-superdry", unique=True)

    def parse(self, response):
        for link in self.link_extractor.extract_links(response):
            with open('ebay2.txt','a+') as f:
                f.write(f"\n{str(link)}")

            yield response.follow(url=link, callback=self.parse)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(Ebayspider)
    process.start()
