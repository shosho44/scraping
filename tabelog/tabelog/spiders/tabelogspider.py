import scrapy


class TabelogspiderSpider(scrapy.Spider):
    name = 'tabelogspider'
    allowed_domains = ['tabelog.com']
    start_urls = ['https://tabelog.com/kyoto/C26100/rstLst/?vs=1&sa=%E4%BA%AC%E9%83%BD%E5%B8%82&sk=%25E3%2583%2599%25E3%2582%25B8%25E3%2582%25BF%25E3%2583%25AA%25E3%2582%25A2%25E3%2583%25B3&lid=top_navi1'
                  '&vac_net=&svd=20210407&svt=1900&svps=2&hfc=1&ChkVegetarianMenu=1&sw=']

    def parse(self, response):
        pass
