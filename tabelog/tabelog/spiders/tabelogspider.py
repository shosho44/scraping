import scrapy


class TabelogspiderSpider(scrapy.Spider):
    name = 'tabelogspider'
    allowed_domains = ['tabelog.com']
    start_urls = ['http://tabelog.com/']

    def parse(self, response):
        pass
