# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class AmzonSpider(RedisCrawlSpider):
    name = 'amzon'
    allowed_domains = ['amazon.cn']
    redis_key = "amzon"

    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='leftNav']//div[@class='a-row a-expander-container a-expander-extend-container']//li",)), follow=True),
        Rule(LinkExtractor(restrict_xpaths=("//div[@id='mainResults']/ul/li//h2/..",)), callback= "parse_item"),
    )

    def parse_item(self, response):
        item = {}
        item["book_img"] = response.xpath("//div[@id='img-canvas']/img/@src").extract_first()
        item["book_author"] = response.xpath("//div[@id='bylineInfo']/span[@class='author notFaded']/a/text()").extract()
        item["book_desc"] = response.xpath("//noscript/div/text()").extract()
        print(item)

