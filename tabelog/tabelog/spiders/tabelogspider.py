import scrapy

import time

import chromedriver_binary
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tabelog.items import TabelogItem

replace_table = str.maketrans({
    '\u3000': '',
    ' ': '',
    '\t': '',
    '\n': '',
    '\r': ''
})


class TabelogspiderSpider(scrapy.Spider):
    name = 'tabelogspider'
    allowed_domains = ['tabelog.com']

    def __init__(self, area='', keyword=''):
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)  # chrome起動
        driver.implicitly_wait(10)
        driver.get('https://tabelog.com/')
        driver.maximize_window()
        
        wait = WebDriverWait(driver, 15)
        
        area_form_css_selector = '#sa'
        area_form_element = driver.find_element_by_css_selector(area_form_css_selector)
        area_form_element.send_keys(area)
        
        time.sleep(1)
        keyword_form_css_selector = '#sk'
        keyword_form_element = driver.find_element_by_css_selector(keyword_form_css_selector)
        keyword_form_element.send_keys(keyword)
        
        time.sleep(1)
        
        search_button_css_selector = '#js-global-search-btn'
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, search_button_css_selector)))
        driver.implicitly_wait(15)
        driver.find_element_by_css_selector(search_button_css_selector).click()
        
        time.sleep(1)
        
        current_url = driver.current_url
        self.start_urls = [current_url]
        
        driver.close()
        
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
        if store_score != '-':
            item['store_score'] = store_score
        is_phone_number = response.css('#column-side > div > div > div > div > div > div > div > p::text').get()
        if is_phone_number is not None:
            phone_number = is_phone_number.translate(replace_table)
            item['phone_number'] = phone_number
        
        table_tr_selectors = response.css('#rst-data-head > table > tbody > tr')
        for table_tr_selector in table_tr_selectors:
            th_content = ''.join(table_tr_selector.css('th ::text').getall())
            td_content = ''.join(table_tr_selector.css('td ::text').getall()).translate(replace_table)
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
                location = td_content.replace('大きな地図を見る周辺のお店を探す', '')
                item['location'] = location
            if '交通手段' in th_content:
                transportation = td_content
                item['transportation'] = transportation
            if 'ドリンク' in th_content:
                drink = td_content
                item['drink'] = drink
            if 'ホームページ' in th_content:
                store_homepage = td_content
                item['store_homepage'] = store_homepage
            if '予算' == th_content:
                budget = td_content
                item['budget'] = budget
            if '禁煙・喫煙' in th_content:
                smoking_ok_or_no = td_content
                item['smoking_ok_or_no'] = smoking_ok_or_no
            if 'お店のPR' in th_content:
                store_strong_point = td_content
                item['store_strong_point'] = store_strong_point

        yield item