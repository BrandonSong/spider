# -*- coding: utf-8 -*-
import scrapy
from yangguang.items import YangguangItem


class YgSpider(scrapy.Spider):
    name = 'yg'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    def parse(self, response):

        tr_list = response.xpath("//div[@class='greyframe']/table[2]/tr//table/tr")

        for tr in tr_list:
            item = YangguangItem()
            item["title"] = tr.xpath("./td[2]/a[2]/text()").extract_first()
            item["status"] = tr.xpath("./td[3]/span/text()").extract_first()
            item["name"] = tr.xpath("./td[4]/text()").extract_first()
            item["publish_date"] = tr.xpath("./td[5]/text()").extract_first()

            # 每个问题详情页的url地址
            detail_url = tr.xpath("./td[2]/a[@class='news14']/@href").extract_first()

            # 请求详情页
            yield scrapy.Request(detail_url,
                                 callback = self.parse_detail,
                                 meta = {"item": item})

        next_url = response.xpath("//a[text()='>']/@href").extract_first()
        if next_url is not None:
            yield scrapy.Request(next_url, callback = self.parse)

    def parse_detail(self, response):
        # 获取列表页中传入的参数
        item = response.meta["item"]
        item["content"] = response.xpath("//div[@class='c1 text14_2']//text()").extract()
        item["img_url"] = response.xpath("//div[@class='c1 text14_2']//img/@src").extract()
        item["img_url"] = ["http://wz.sun0769.com" + i for i in item["img_url"]]
        yield item
