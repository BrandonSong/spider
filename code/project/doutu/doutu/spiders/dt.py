# -*- coding: utf-8 -*-
import scrapy
from doutu.items import DoutuItem
from urllib.parse import urljoin

class DtSpider(scrapy.Spider):
    name = 'dt'
    allowed_domains = ['doutula.com']
    start_urls = ['https://www.doutula.com/article/list/']

    def parse(self, response):

        pic_list = response.xpath("//div[@class='col-sm-9']/a")
        for pic in pic_list:
            url = pic.xpath("./@href").extract_first()
            yield scrapy.Request(url,callback=self.parse_img)

        next_url = response.xpath("//ul[@class='pagination']/li/a[text()='›']/@href").extract_first()
        next_url = urljoin(response.url, next_url)
        yield scrapy.Request(next_url, callback=self.parse)

    def parse_img(self, response):
        div_list = response.xpath("//div[@class='pic-content']/div[@class='artile_des']")
        for div in div_list:
            item = DoutuItem()
            item["image_urls"] = div.xpath(".//img/@src").extract()
            print(item)
            yield item