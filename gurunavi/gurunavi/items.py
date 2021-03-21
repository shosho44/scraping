# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GurunaviItem(scrapy.Item):
    # define the fields for your item here like:
    store_name = scrapy.Field()  # 店名
    phone_num = scrapy.Field()  # 電話番号
    postal_code = scrapy.Field()  # 郵便番号
    location = scrapy.Field()  # 場所
    opening_hours = scrapy.Field()  # 営業時間
    regular_holiday = scrapy.Field()  # 定休日
    gurunavi_url = scrapy.Field()  # ぐるなびのurl
    genre = scrapy.Field()  # ジャンル
    key_word = scrapy.Field()
    pass
