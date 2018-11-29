# -*- coding: utf-8 -*-
import scrapy


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr[@class='even'] | //table[@class='tablelist']/tr[@class='odd']")

        for tr in tr_list:
          item = dict()
          position_name = tr.xpath("./td[1]/a/text()").extract_first()
          position_type = tr.xpath("./td[2]/text()").extract_first()
          position_people = tr.xpath("./td[3]/text()").extract_first()
          position_addr = tr.xpath("./td[4]/text()").extract_first()
          position_date = tr.xpath("./td[5]/text()").extract_first()

          item["position_name"] = position_name
          item["position_type"] = position_type
          item["position_people"] = position_people
          item["position_addr"] = position_addr
          item["position_date"] = position_date
          yield item
        next_page_url = response.xpath("//a[@id='next']/@href").extract_first()

        if next_page_url != "javascript:;":
            next_url = "https://hr.tencent.com/" + next_page_url
            yield scrapy.Request(next_url, callback = self.parse)