# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YangguangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()  # 问政标题
    status = scrapy.Field()  # 当前状态
    name = scrapy.Field()  # 投诉人
    publish_date = scrapy.Field()  # 投诉时间
    content = scrapy.Field()  # 投诉内容
    img_url = scrapy.Field()  # 内容图片
