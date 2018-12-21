# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoutuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    image_name = scrapy.Field()
    # 此字段用来记录要下载的图片的url地址 并且此字段值必须为可以迭代对象 如列表 否则会报错
    image_urls = scrapy.Field()
