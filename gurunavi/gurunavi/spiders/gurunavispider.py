import scrapy


class GurunavispiderSpider(scrapy.Spider):
    name = 'gurunavispider'
    allowed_domains = ['https://r.gnavi.co.jp/area/jp/rs/?fwr=%E3%83%99%E3%82%B8%E3%82%BF%E3%83%AA%E3%82%A2%E3%83%B3']
    start_urls = ['http://https://r.gnavi.co.jp/area/jp/rs/?fwr=%E3%83%99%E3%82%B8%E3%82%BF%E3%83%AA%E3%82%A2%E3%83%B3/']

    def parse(self, response):
        pass
