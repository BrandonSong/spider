# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/module14430/page1.htm']

    rules = (
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = dict()
        item["title"] = response.xpath()
        item["title"] = response.xpath()
        item["title"] = response.xpath()
