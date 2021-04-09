import scrapy

from tabelog.items import TabelogItem

class TabelogspiderSpider(scrapy.Spider):
    name = 'tabelogspider'
    allowed_domains = ['tabelog.com']
    start_urls = ['https://tabelog.com/kyoto/C26100/rstLst/?vs=1&sa=%E4%BA%AC%E9%83%BD%E5%B8%82&sk=%25E3%2583%2599%25E3%2582%25B8%25E3%2582%25BF%25E3%2583%25AA%25E3%2582%25A2%25E3%2583%25B3&lid=top_navi1'
                  '&vac_net=&svd=20210407&svt=1900&svps=2&hfc=1&ChkVegetarianMenu=1&sw=']

    def parse(self, response):
        article_urls_list = response.css('#container > div.rstlist-contents.clearfix > div.flexible-rstlst > div > div.js-rstlist-info.rstlist-info > div > div.list-rst__wrap.js-open-new-window > div > div.list-rst__contents > div > div.list-rst__rst-name-wrap > h4 > a::attr("href")').getall()
        for article_url in article_urls_list:
            yield scrapy.Request(article_url, self.get_info)
        
        is_pagination = response.css('#container > div.rstlist-contents.clearfix > div.flexible-rstlst > div > div.list-pagenation > div > ul > li > a[rel="next"]::attr("href")').get()
        if is_pagination:
            next_page_url = is_pagination
            yield scrapy.Request(next_page_url, self.parse)
    
    def get_info(self, response):
        item = TabelogItem()

        item['store_url_of_tabelog'] = response.url
        store_score = response.css('#js-detail-score-open > p > b > span::text').get()
        item['score_score'] = store_score
        is_phone_number = response.css('#column-side > div > div > div > div > div > div > div > p::text').get()
        if is_phone_number is not None:
            phone_number = is_phone_number
            item['phone_number'] = phone_number
        
        table_tr_selectors = response.css('#rst-data-head > table > tbody > tr')
        for table_tr_selector in table_tr_selectors:
            th_content = ''.join(table_tr_selector.css('th ::text').getall())
            td_content = ''.join(table_td_selector.css('td ::text').getall())
            if '店名' in th_content:
                store_name = td_content
                item['store_name'] = store_name
            if 'ジャンル' in th_content:
                genre = td_content
                item['genre'] = genre
            if '予約可否' in th_content:
                reservation_availability = td_content
                item['reservation_availability'] = reservation_availability
            if '住所' in th_content:
                location = td_content
                item['location'] = location
            if '交通手段' in th_content:
                transportaton = td_content
                item['transportation'] = transportaton
            if 'ホームページ' in th_content:
                store_homepage = td_content
                item['store_homepage'] = store_homepage
            if '予算' == th_content:
                budget = td_content
                item['budget'] = budget

        yield item