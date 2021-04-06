# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TabelogItem(scrapy.Item):
    store_url_of_tabelog = scrapy.Field() #url
    location = scrapy.Field()  # 店舗住所
    store_name = scrapy.Field()  # 店名
    genre = scrapy.Field()  # ジャンル
    open_day = scrapy.Field()  # 営業時間
    phone_number = scrapy.Field()  # 電話番号
    store_url = scrapy.Field()  # お店のurl
    budget_night = scrapy.Field()  # 夜の価格帯
    budget_noon = scrapy.Field()  # 昼の価格帯
    star_num = scrapy.Field()  # 星の数