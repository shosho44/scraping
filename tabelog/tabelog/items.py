# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TabelogItem(scrapy.Item):
    store_url_of_tabelog = scrapy.Field()  # 店舗の食べログurl
    location = scrapy.Field()  # 店舗住所
    store_name = scrapy.Field()  # 店名
    genre = scrapy.Field()  # 食べ物のジャンル
    phone_number = scrapy.Field()  # 電話番号
    store_homepage = scrapy.Field()  # 店舗のホームページ
    reservation_availability = scrapy.Field()  # 予約可能かどうか
    transportation = scrapy.Field()  # 交通手段
    store_score = scrapy.Field()  # 星評価数
    budget = scrapy.Field()  # 予算
    store_strong_point = scrapy.Field()  # お店のPR
    drink = scrapy.Field()  # ドリンクの種類
    smoking_ok_or_no = scrapy.Field()  # 喫煙禁煙どちらか