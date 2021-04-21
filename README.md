# Scrapy18

### Demonstration of how to read a list of URLs from a CSV (and use in Scrapy)

    with open('data.csv') as file:
        start_urls = [line.strip() for line in file]

#### use start_urls as the url for each request made by start_request method

    def start_request(self):
        request = Request(url = self.start_urls, callback=self.parse)
        yield request
        
https://redandgreen.co.uk/scrapy-start_urls-from-csv/
