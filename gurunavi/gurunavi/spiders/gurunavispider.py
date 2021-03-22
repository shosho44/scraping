import scrapy


class GurunavispiderSpider(scrapy.Spider):
    name = 'gurunavispider'
    allowed_domains = ['r.gnavi.co.jp']
    start_urls = ['http://https://r.gnavi.co.jp/area/jp/rs/?fwr=%E3%83%99%E3%82%B8%E3%82%BF%E3%83%AA%E3%82%A2%E3%83%B3/',
                  'https://r.gnavi.co.jp/area/jp/rs/?fwr=%E3%83%B4%E3%82%A3%E3%83%BC%E3%82%AC%E3%83%B3']

    def parse(self, response):
        store_url_list = response.css('div > div.result-cassette__box-inner > div.result-cassette__box-main > div.result-cassette__box-head > div > a::attr("href")').getall()
        
        # 各記事に移動
        for store_url in store_url_list:
            yield scrapy.Request(store_url, self.xxxx)

        # ページネーション
        is_next_page_url_list = response.css('div.layout__pagination > div > nav > div > ul > li.pagination__arrow-item > a.pagination__arrow-item-inner-next::attr("href")').getall()
        if is_next_page_url_list:
            next_page_url = is_next_page_url_list[0]
            yield scrapy.Request(next_page_url, self.parse)