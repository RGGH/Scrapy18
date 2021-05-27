# -*- coding: utf-8 -*-
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

import os

import scrapy
from scrapy import Request
from scrapy.crawler import CrawlerProcess 
from bs4 import BeautifulSoup

import sys
sys.path.insert(0,'..')
from items import JobsItem


class Jobs(scrapy.Spider):			

    name = 'jobs' 
    start_urls = ['https://uk.jooble.org/SearchResult?date=8&loc=2&p=2&rgns=Remote&ukw=python%20engineer']
    headers = {'sec-fetch-user': '?1', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 'accept-encoding': 'gzip,', 'sec-fetch-site': 'same-origin', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'upgrade-insecure-requests': '1', 'referer': 'https://www.jooble.org/', 'sec-fetch-mode': 'navigate', 'cache-control': 'max-age=0', 'user-agent': ' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36', 'sec-fetch-dest': 'document'}
    custom_settings = {'FEEDS':{'jobs1.csv':{'format':'csv'}}}

    def parse(self, response):
        
        links = response.xpath('//h2/a/@href').getall()
        #print(links)
        for link in links:        
            yield response.follow(url=link, headers=self.headers, callback=self.parse_detail)
            print(response.url)

    def parse_detail(self, response):

        #items = JobsItem()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        desc = soup.get_text()
        url = response.url

        yield {'desc':desc,'url':url}


# main driver
if __name__ =='__main__':
    process = CrawlerProcess()
    process.crawl(Jobs)
    process.start()
