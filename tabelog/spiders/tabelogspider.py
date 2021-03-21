import scrapy
import re

from tabelog.items import TabelogItem


table = str.maketrans({
    '\u3000': '',
    ' ': '',
    '\t': '',
    "\n": ""
})


class TabelogspiderSpider(scrapy.Spider):
    name = 'tabelogspider'
    allowed_domains = ['tabelog.com']
    start_urls = ['https://tabelog.com/hokkaido/rstLst/60/?Srt=D&SrtT=rt&sort_mode=1']


    def parse(self, response):
        pref_list = ['aomori', 'akita', 'iwate', 'miyagi', 'yamagata', 'fukushima', 'ibaraki', 'tochigi', 'gunma', 'saitama', 'chiba', 'niigata', 'toyama', 'ishikawa', 'fukui', 'yamanashi', 'nagano', 'gifu', 'shizuoka', 'mie', 'shiga', 'hyogo', 'nara', 'wakayama', 'tottori', 'shimane', 'okayama', 'hiroshima', 'yamaguchi', 'tokushima', 'kagawa', 'ehime', 'kochi', 'fukuoka', 'saga', 'nagasaki', 'kumamoto', 'oita', 'miyazaki','kagoshima','okinawa', 'hokkaido', 'tokyo', 'kanagawa', 'aichi', 'osaka', 'kyoto']
        url_of_sitemap_list = ['https://tabelog.com/sitemap/hokkaido/', 'https://tabelog.com/sitemap/tokyo/', 'https://tabelog.com/sitemap/kanagawa/', 'https://tabelog.com/sitemap/aichi/', 'https://tabelog.com/sitemap/osaka/', 'https://tabelog.com/sitemap/kyoto/']

        for pref_chr in pref_list:
            if pref_chr in {'hokkaido', 'tokyo', 'kanagawa', 'aichi', 'osaka', 'kyoto'}:
                for url_of_pref_from_sitemap in url_of_sitemap_list:
                    yield scrapy.Request(url_of_pref_from_sitemap, callback = self.get_url_of_area)
            else:
                url_connect_head_chr = 'https://tabelog.com/'
                url_connect_tale_chr = '/rstLst/?Srt=D&SrtT=rt&sort_mode=1'
                pref_url = url_connect_head_chr + pref_chr + url_connect_tale_chr
                yield scrapy.Request(pref_url, callback = self.get_store_url_and_map_url_and_pagenation)


    def get_url_of_area(self, response):
        url_of_all_detail_area = response.css('#arealst_sitemap li a::attr(href)').getall()
        for url_of_detail_area in url_of_all_detail_area:
            url_of_ranking_detail_area = url_of_detail_area.replace("sitemap/","").replace("-","/") + "rstLst/?SrtT=rt&Srt=D&sort_mode=1"
            yield scrapy.Request(url_of_ranking_detail_area, callback = self.get_store_url_and_map_url_and_pagenation)



    def get_store_url_and_map_url_and_pagenation(self, response):#pagenation
        all_store_url_in_a_page = response.css('.list-rst__rst-name-wrap .list-rst__rst-name-target::attr(href)').getall()
        length_of_all_store_url_in_a_page_list = len(all_store_url_in_a_page)

        for index_num in range(length_of_all_store_url_in_a_page_list):
            item = TabelogItem()

            store_url_of_tabelog = all_store_url_in_a_page[index_num]
            item['store_url_of_tabelog'] = store_url_of_tabelog
            store_map_url = all_store_url_in_a_page[index_num] + "dtlmap/"
            yield scrapy.Request(store_map_url, callback = self.get_all_information, meta = {'item': item})

        url_of_pagenation = response.css(".list-pagenation .c-pagination .c-pagination__list a[rel='next']::attr(href)").get()
        if url_of_pagenation:
            yield scrapy.Request(url_of_pagenation, self.get_store_url_and_map_url_and_pagenation)



    def get_all_information(self, response):
        item = response.meta['item']

        location = response.css(".map-rstinfo td").xpath('string()').get().replace(" ","").replace("\n"," ").translate(table)
        item['location'] = location


        th_all_content = response.css("#rst-data-head th").xpath('string()').getall()
        td_all_content = response.css("#rst-data-head td").xpath('string()').getall()
        for th_content in th_all_content:
            if "店名" in th_content:
                store_name_th_index = th_all_content.index(th_content)
                store_name = td_all_content[store_name_th_index].translate(table)
                item['store_name'] = store_name

            if "ジャンル" in th_content:
                genre_th_index = th_all_content.index(th_content)
                genre = td_all_content[genre_th_index].translate(table)
                item['genre'] = genre

            if "お問い合わせ" in th_content:
                phone_number_th_index = th_all_content.index(th_content)
                phone_number = td_all_content[phone_number_th_index].translate(table)
                if phone_number != '不明の為情報お待ちしております':
                    item['phone_number'] = phone_number

            if "席数" in th_content:
                seats_th_index = th_all_content.index(th_content)
                seats_txt = td_all_content[seats_th_index].translate(table)
                search_seats_by_regix_result = re.search(r'\d{1,5}席', seats_txt)
                if search_seats_by_regix_result is not None:
                    seats = search_seats_by_regix_result.group()
                    item['seats'] = seats

            if "ホームページ" in th_content:
                store_url_th_index = th_all_content.index(th_content)
                store_url = td_all_content[store_url_th_index].translate(table)
                item['store_url'] = store_url

        yield item
