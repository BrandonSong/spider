# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtmsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    store_name = scrapy.Field()
    category = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    consumption = scrapy.Field()
    shop_hours = scrapy.Field()
    score = scrapy.Field()
    score_num = scrapy.Field()
