# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ziru.items import ZiruItem



class ZrSpider(CrawlSpider):
    name = 'zr'
    allowed_domains = ['ziroom.com']
    start_urls = ['http://sh.ziroom.com/z/nl/z2.html']

    rules = (
        Rule(LinkExtractor(allow=r'//sh.ziroom.com/z/nl/z\d+.html')),
        Rule(LinkExtractor(allow=r'//sh.ziroom.com/z/vr/\d+.html'), callback='parse_house_list'),
        Rule(LinkExtractor(allow=r'//sh.ziroom.com/z/nl/z\d+.html?p=\d+'), follow=True),
    )

    def parse_house_list(self, response):
       """此函数获取房屋列表"""
       item = ZiruItem()

       item["room_href"]  = response.url
       item["room_name"] = response.xpath("//div[@class='room_name']/h2/text()").extract_first().strip()
       item["room_addr"] = response.xpath("//div[@class='room_name']/p/span/text()").extract_first().replace(" ", "")

       # 获取房屋的详细信息
       item["room_area"] = response.xpath("//ul[@class='detail_room']/li[1]/text()").extract_first().strip()
       item["room_orientations"] = response.xpath("//ul[@class='detail_room']/li[2]/text()").extract_first().strip()
       item["room_type"] = response.xpath("//ul[@class='detail_room']/li[3]/text()").extract_first().strip()
       item["room_floor"] = response.xpath("//ul[@class='detail_room']/li[4]/text()").extract_first().strip()
       item["room_traffic"] = response.xpath("//ul[@class='detail_room']/li[5]/span[@class='lineList']/text()").extract()

       item["room_desc"] = response.xpath("//div[@class='aboutRoom gray-6']/p/text()").extract_first().strip()
       item["room_allocation"]  = response.xpath("//div[@id='configBox']/ul/li/text()").extract()

       yield item
