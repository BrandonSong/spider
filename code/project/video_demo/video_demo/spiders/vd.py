# -*- coding: utf-8 -*-
import scrapy


class VdSpider(scrapy.Spider):
    name = 'vd'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/video/av26677941/']

    def parse(self, response):
        pass
