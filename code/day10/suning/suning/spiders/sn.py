# -*- coding: utf-8 -*-
import scrapy
from suning.items import SuningItem


class SnSpider(scrapy.Spider):
    name = 'sn'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        # 获取分类名和分类的url
        ul_list = response.xpath("//ul[@class='book-name-list clearfix']")
        for ul in ul_list:
            item = SuningItem()
            item["category"] = ul.xpath("./li/a/text()").extract_first()
            category_url = ul.xpath("./li/a/@href").extract_first()

            yield scrapy.Request(category_url, callback=self.parse_book_list, meta={"item": item})

    def parse_book_list(self, response):
        item = response.meta["item"]

        # 获取当前页的书籍
        li_list = response.xpath("//ul[@class='clearfix']/li")
        for li in li_list:
            book_part_url = li.xpath(".//div[@class='img-block']/a/@href").extract_first()
            book_url = "https:" + book_part_url
            yield scrapy.Request(book_url, callback=self.parse_book_detail, meta={"item": item})

        # 1.获取下一页url
        next_part_url = response.xpath("//div[@id='bottom_pager']/a[@id='nextPage']/@href").extract_first()
        # 2.如果下一页url存在,发送请求
        if next_part_url is not None:
            next_url = "https://list.suning.com" + next_part_url
            yield scrapy.Request(next_url, callback = self.parse_book_list)

    def parse_book_detail(self, response):
        item = response.meta["item"]

        item["book_name"] = response.xpath("//h1[@id='itemDisplayName']/text()").extract_first()
        pb_items = response.xpath("//ul[@class='bk-publish clearfix']/li")
        if len(pb_items) > 2:
            item["book_author"] = response.xpath("//ul[@class='bk-publish clearfix']/li[1]/text()").extract_first()
            item["publish_house"] = response.xpath("//ul[@class='bk-publish clearfix']/li[2]/text()").extract_first()
            item["publish_date"] = response.xpath("//ul[@class='bk-publish clearfix']/li[3]/span[2]/text()").extract_first()
        else:
            item["publish_house"] = response.xpath("//ul[@class='bk-publish clearfix']/li[1]/text()").extract_first()
            item["publish_date"] = response.xpath("//ul[@class='bk-publish clearfix']/li[2]/span[2]/text()").extract_first()

        yield item

