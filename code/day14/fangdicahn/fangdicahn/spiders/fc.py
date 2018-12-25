# -*- coding: utf-8 -*-
import scrapy
import json
from urllib.parse import urljoin
import re
from lxml import etree

class FcSpider(scrapy.Spider):
    name = 'fc'
    allowed_domains = ['fangdi.com.cn']
    start_urls = ['http://www.fangdi.com.cn/service/index/getWriteDict.action']
    url = "http://www.fangdi.com.cn/service/freshHouse/getHosueList.action"


    # 重写start_request方法来起始请求为post方式请求
    def start_requests(self):
        yield scrapy.FormRequest(url = self.start_urls[0], formdata = {"dict": "dic_lm_512"}, callback= self.parse)

    def parse(self, response):
        """ 解析区域信息 发送请求 获取每个区域房屋信息 """
        json_data = json.loads(response.body.decode())
        # 获取地区信息列表
        zone_list = json_data.get('listWriteDict')
        code = zone_list[0].get("code")
        print("获取的是",zone_list[0].get("name"))
        yield scrapy.Request(url = self.url, method = "POST", body = json.dumps({"districtID": code, "currentPage": "1"}), callback = self.parse_house)

        # 循环所有的区域
        # for zone in zone_list:
        #     code = zone.get('code')
        #
        #
        #     yield scrapy.Request(url =url, method = "POST",body = json.dumps({"districtID": code, "currentPage": "1"}), callback = self.parse_house)

    def parse_house(self, response):

        page_source = response.body.decode()
        req_body = json.loads(response.request.body.decode())
        currentPage = int(req_body["currentPage"])


        json_data = json.loads(page_source)
        html_str = etree.HTML(json_data.get("htmlView"))

        # 获取房屋信息
        # tr_list = html_str.xpath("//table/tbody/tr")
        # for tr in tr_list:
        #     item = dict()
        #     status = tr.xpath("./td[1]/text()")[0]
        #     if status == "2":
        #         status = "在售"
        #     elif status == "4":
        #         status = "售完"
        #     elif status == "8":
        #         status = "暂停销售"
        #     project = tr.xpath("./td[2]/a/text()")[0]
        #     address = tr.xpath("./td[3]/text()")[0]
        #     total_num = tr.xpath("./td[4]/text()")[0]
        #     total_area = tr.xpath("./td[5]/text()")[0]
        #     zone = tr.xpath("./td[6]/text()")[0]
        #     item = {
        #         "status": status,
        #         "project": project,
        #         "address": address,
        #         "total_num": total_num,
        #         "total_area": total_area,
        #         "zone": zone
        #     }
        #     yield  item



        pageCount = int(html_str.xpath("//input[@id='PageCount']/@value")[0])

        print("总共",pageCount)
        if currentPage <= pageCount:
            req_body["currentPage"] = str(currentPage + 1)

            print(req_body["currentPage"])
            yield scrapy.Request(response.request.url,
                            method = "POST",
                            body = json.dumps(req_body),
                            callback = self.parse_house,
                            dont_filter = True)
        else:
            print("已经没有了")

