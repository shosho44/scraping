import scrapy
from gurunavi.items import GurunaviItem

import re


class GurunavispiderSpider(scrapy.Spider):
    name = 'gurunavispider'
    allowed_domains = ['r.gnavi.co.jp']
    start_urls = ['https://r.gnavi.co.jp/area/jp/rs/?fwr=%E3%83%99%E3%82%B8%E3%82%BF%E3%83%AA%E3%82%A2%E3%83%B3/',
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
        
    # itemのフィールドに入れる情報取得
    def get_info(self, response):
        item = GurunaviItem()
        selector_table_contents = response.css('#info-table > table > tbody > tr')
        itme['key_word'] = 'ベジタリアン'
        phone_num = ''.join(response.css('#nav-ex > nav > div > div > span::text').getall()).replace(' ', '').replace('\n', '')
        item['phone_num'] = phone_num
        item['gurunavi_url'] = response.url()
        for selector_table_content in selector_table_contents:
            # テーブルの項目
            th_content = selector_table_content.css('th::text').get()
            # 項目の内容
            td_content = selector_table_content.css('td::text').get()

            if '店名' in th_content:
                store_name = td_content
                item['store_name'] = store_name

            if '住所' in th_content:
                postal_code_and_locataion = td_content
                pattern_postal_code = r'(\d{3})-(\d{4})'
                is_postal_code = pattern_postal_code.search(td_content)
                if is_postal_code:
                    postal_code = is_postal_code.group()
                    item['postal_code'] = postal_code
                    location = postal_code_and_locataion.replace(postal_code, '')
                    item['location'] = location
            
            if '営業時間' in th_content:
                opening_hours = td_content
                item['opening_hours'] = opening_hours
            
            if '定休日' in th_content:
                regular_holiday = td_content
                item['regular_holiday'] = regular_holiday
                
            if 'food_genre' in th_content:
                food_genre = td_content
                item['food_genre'] = food_genre

        yield item
