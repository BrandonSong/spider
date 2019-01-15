# -*- coding: utf-8 -*-
import scrapy
import re
import json
from mtms.items import MtmsItem


class MsSpider(scrapy.Spider):
    name = 'ms'
    allowed_domains = ['meituan.com']
    start_urls = ['http://meishi.meituan.com/i/?ci=10']
    cookies_url = 'http://i.meituan.com/'

    custom_settings = {
        "headers": {
            "Content-Type": "application/json",
            "Refer": "http://meishi.meituan.com/i/?ci=10",
        }
    }

    def start_requests(self):
        yield scrapy.Request(url=self.cookies_url, callback=self.get_cookies)

    def get_cookies(self, response):
        print("开始抓取")
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):

        print("准备解析请求参数")

        data = response.body.decode()
        ret = re.findall("window._appState = (.*);</script>", data)[0]
        json_data = json.loads(ret)

        cateList = json_data['navBarData']['categoryList']
        # areaList = json_data['navBarData']['areaList']

        areaList = json_data['navBarData']['areaObj']
        uuid = json_data['$meta']['uuid']

        for cate in cateList:
            yield scrapy.Request(
                url= "http://meishi.meituan.com/i/api/region/list",
                method = "POST",
                body = json.dumps({"cateId": int(cate["id"])}),
                headers = self.custom_settings['headers'],
                dont_filter = True,
                callback = self.parse_region,
                meta = {"cateId": cate["id"], "uuid": uuid}
            )



        # for cate in cateList[1:]:
        #     for key, areaValue in areaList.items():
        #         for area in areaValue:
        #             if area['name'] != '全部':
        #                 limit = 15
        #                 offset = 0
        #                 print(area["name"], cate["name"], "共有", area["count"], "条数据获取完成")
        #                 while True:
        #                     form_body = {
        #                         "app": "",
        #                         "areaId": int(area['id']),
        #                         "cateId": int(cate['id']),
        #                         "deal_attr_23": "",
        #                         "deal_attr_24": "",
        #                         "deal_attr_25": "",
        #                         "limit": limit,
        #                         "lineId": 0,
        #                         "offset": offset,
        #                         "optimusCode": 10,
        #                         "originUrl": "http://meishi.meituan.com/i/?ci=10",
        #                         "partner": 126,
        #                         "platform": 3,
        #                         "poi_attr_20033": "",
        #                         "poi_attr_20043": "",
        #                         "riskLevel": 1,
        #                         "sort": "default",
        #                         "stationId": 0,
        #                         "uuid": uuid,
        #                         "version": "8.3.3"
        #                     }
        #
        #                     yield scrapy.Request(url='http://meishi.meituan.com/i/api/channel/deal/list',
        #                                          method='POST',
        #                                          body=json.dumps(form_body),
        #                                          headers=self.custom_settings['headers'],
        #                                          dont_filter=True,
        #                                          callback=self.parse_store
        #                                          )
        #
        #                     if (limit + offset) > int(area['count']):
        #                         print(area["name"], cate["name"],"共有", area["count"],"条数据获取完成")
        #                         # break
        #                         return
        #
        #                     else:
        #                         print(offset)
        #                         offset += 15


    def parse_region(self, response):

        cateId = response.meta.get('cateId')
        uuid = response.meta.get('uuid')

        data = response.body.decode()

        json_data = json.loads(data)

        areaList = json_data["data"]["areaList"]

        for area in areaList:
            if area["name"] != "全城":
                limit = 15
                offset = 0
                while True:
                    form_body = {"app": "",
                                "areaId": int(area['id']),
                                "cateId": int(cateId),
                                "deal_attr_23": "",
                                "deal_attr_24": "",
                                "deal_attr_25": "",
                                "limit": limit,
                                "lineId": 0,
                                "offset": offset,
                                "optimusCode": 10,
                                "originUrl": "http://meishi.meituan.com/i/?ci=10",
                                "partner": 126,
                                "platform": 3,
                                "poi_attr_20033": "",
                                "poi_attr_20043": "",
                                "riskLevel": 1,
                                "sort": "default",
                                "stationId": 0,
                                "uuid": uuid,
                                "version": "8.3.3"}

                    yield scrapy.Request(url = 'http://meishi.meituan.com/i/api/channel/deal/list',
                                                             method='POST',
                                                             body=json.dumps(form_body),
                                                             headers=self.custom_settings['headers'],
                                                             dont_filter=True,
                                                             callback=self.parse_store)
                    if offset > area["count"]:
                        print(area['name'], area['count'])
                        break
                    else:
                        offset += 15

    def parse_store(self, response):
        print("解析详情页数据")

        data = response.body.decode()

        json_data = json.loads(data)
        try:
            store_infos = json_data['data']['poiList']['poiInfos']

            for store in store_infos:
                ct_poi = store['ctPoi']
                poi_id = store['poiid']
                cateName = store['cateName']
                yield scrapy.Request(
                    url="http://meishi.meituan.com/i/poi/{}?{}".format(poi_id, ct_poi),
                    callback=self.parse_detail,
                    meta= {"cateName": cateName}
                )
        except:
            print(json_data)


    def parse_detail(self, response):

        ms = MtmsItem()

        print("开始提取数据")

        cateName = response.meta.get('cateName', None)

        data = response.body.decode()
        ret = re.findall("window._appState = (.*);</script>", data)[0]
        json_data = json.loads(ret)

        store_name = json_data['poiInfo']['name']
        address = json_data['poiInfo']['addr']
        phone = json_data['poiInfo']['phone']
        avgPrice = json_data['poiInfo']['avgPrice']
        shop_hours = json_data['poiInfo']['openInfo']
        score = json_data['poiInfo']['avgScore']
        score_num = json_data['poiInfo']['MarkNumbers']


        ms['store_name']= store_name
        ms['address']= address
        ms['phone']= phone
        ms['avgPrice']= avgPrice
        ms['shop_hours']= shop_hours
        ms['score']= score
        ms['score_num']= score_num
        ms['category'] = cateName

        yield ms
