import scrapy


class TabelogspiderSpider(scrapy.Spider):
    name = 'tabelogspider'
    allowed_domains = ['tabelog.com']
    start_urls = ['https://tabelog.com/kyoto/C26100/rstLst/?vs=1&sa=%E4%BA%AC%E9%83%BD%E5%B8%82&sk=%25E3%2583%2599%25E3%2582%25B8%25E3%2582%25BF%25E3%2583%25AA%25E3%2582%25A2%25E3%2583%25B3&lid=top_navi1'
                  '&vac_net=&svd=20210407&svt=1900&svps=2&hfc=1&ChkVegetarianMenu=1&sw=']

    def parse(self, response):
        article_urls_list = response.css('#container > div.rstlist-contents.clearfix > div.flexible-rstlst > div > div.js-rstlist-info.rstlist-info > div > div.list-rst__wrap.js-open-new-window > div > div.list-rst__contents > div > div.list-rst__rst-name-wrap > h4 > a::attr("href")').getall()
        for article_url in article_urls_list:
            yield scrapy.Request(article_url, self.store_detail_url)
        
        is_pagination = response.css('#container > div.rstlist-contents.clearfix > div.flexible-rstlst > div > div.list-pagenation > div > ul > li > a[rel="next"]::attr("href")').get()
        if is_pagination:
            next_page_url = is_pagination
            yield scrapy.Request(next_page_url, self.parse)
        
    def get_store_detail_url(self, response):
        store_detail_url = response.css('#rdnavi-coupon > div > a::attr("href")').get()
        yield scrapy.Request(store_detail_url, self.get_info)
    
    def get_info(self, response):
        pass