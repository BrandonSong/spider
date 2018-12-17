# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZiruItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    room_href = scrapy.Field()
    room_name = scrapy.Field()
    room_price = scrapy.Field()
    room_area = scrapy.Field()
    room_orientations = scrapy.Field()
    room_addr = scrapy.Field()
    room_type = scrapy.Field()
    room_floor = scrapy.Field()
    room_traffic = scrapy.Field()
    room_desc = scrapy.Field()
    room_allocation = scrapy.Field()
