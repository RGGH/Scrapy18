import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract

class Lakspider(Spider):
    name = 'lakspider'

    # read csv with just url per line
    with open('urls.csv') as file:
        start_urls = [line.strip() for line in file]

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        yield request
    
    def parse(self, response):
    
            html = response.body
            soup = BeautifulSoup(html, 'lxml')
            text = soup.get_text()
            
            # add more specific here if required 
            # eg title = soup.find("title")
            #    heading = soup.find("h1")
    
            # get the domain for the file name
            domain = tldextract.extract(response.request.url)[1]
            path = urlparse(response.request.url)[2].replace("/", "")
    
            # export the text
            with open(f'{domain}.txt', 'a') as fp:
                fp.write(text)
                
            # export the html
            with open(f'{domain} {path}.html', 'wb') as fp:
                fp.write(response.body)

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(Lakspider)
    process.start()
