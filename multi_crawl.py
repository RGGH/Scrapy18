# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess
from scrapy import Request

class LkSpider(CrawlSpider):
    name = 'multi_spider'

    # read csv with just url per line
    with open('urls.csv') as file:
        start_urls = [line.strip() for line in file]

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        yield request
 

    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        
        #description is the text from all the paragraphs 
        descriptions = response.xpath('*//p/text()').getall()
        description = ''.join(descriptions)
        description = description[:999]
        
        # create file in an output folder, with name of domain followed by name of page
        filename = response.url.split("/")[-2] + '.txt'
        with open(filename, 'w') as f:
            f.write(description)

# main driver
if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(LkSpider)
    process.start()
