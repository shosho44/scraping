# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TabelogItem(scrapy.Item):
    store_url_of_tabelog = scrapy.Field() #url
    location = scrapy.Field() #店舗住所
    store_name = scrapy.Field() #店名
    genre = scrapy.Field() #ジャンル
    phone_number = scrapy.Field() #電話番号
    store_url = scrapy.Field() #お店のurl
    seats = scrapy.Field() #席数
