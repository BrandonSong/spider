# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TbSpider(CrawlSpider):
    name = 'tb'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=LOL']

    rules = (
        Rule(LinkExtractor(allow=r'/p/\d+'), callback='parse_item'),
        # Rule(LinkExtractor(allow=r'//tieba.baidu.com/f?kw=lol&ie=utf-8&pn=\d+', restrict_xpaths="//a[@class='next pagination-item ']"), follow=True),
        Rule(LinkExtractor(allow=r'&ie=utf-8&pn=\d+', restrict_xpaths="//a[@class='next pagination-item ']"), follow=True),
    )

    def parse_item(self, response):
        item = dict()
        item["title"] = response.xpath("//meta[@name='description']/@content").extract_first()
        print(item)
