# -*- coding: utf-8 -*-
import scrapy
import re
import json


class MsSpider(scrapy.Spider):
    name = 'ms'
    allowed_domains = ['meituan.com']
    start_urls = ['http://meishi.meituan.com/i/?ci=10']

    def parse(self, response):

        # data = response.body.decode()
        # ret = re.findall("window._appState = (.*);</script>", data)[0]
        # json_data = json.loads(ret)
        #
        # cateList = json_data['navBarData']['categoryList']
        # areaList = json_data['areaList']
        # uuid = json_data['uuid']

        print("准备进入")

        form_body = {
                    "app": "",
                    "areaId": 280,
                    "cateId": 20097,
                    "deal_attr_23": "",
                    "deal_attr_24": "",
                    "deal_attr_25": "",
                    "limit": 15,
                    "lineId": 0,
                    "offset": 0,
                    "optimusCode": 10,
                    "originUrl": "http://meishi.meituan.com/i/?ci=10",
                    "partner": 126,
                    "platform": 3,
                    "poi_attr_20033": "",
                    "poi_attr_20043": "",
                    "riskLevel": 1,
                    "sort": "default",
                    "stationId": 0,
                    "uuid": "f351320b3eeb4c939f58.1547436545.1.0.0",
                    "version": "8.3.3"
                }

        headers = {
            "Content-Type": "application/json",
            "Refer": "http://meishi.meituan.com/i/?ci=10",
        }

        cookies = {
            "Cookie": "__mta=245831611.1547436569676.1547447739278.1547455112265.10; _lxsdk_cuid=164e9fbb0ddc8-046b6b0d4ef04a-5e442e19-1fa400-164e9fbb0dec8; _ga=GA1.2.484326599.1532933944; iuuid=5013A50AE6242FBEEF6AA56A6809FD693B123047B4DFB8966E85A2CA43DC6F44; ci=10; cityname=%E4%B8%8A%E6%B5%B7; _lxsdk=5013A50AE6242FBEEF6AA56A6809FD693B123047B4DFB8966E85A2CA43DC6F44; _hc.v=6f8ef646-03ae-63ac-1485-ecea7fe925fd.1537243990; webp=1; Hm_lvt_f66b37722f586a240d4621318a5a6ebe=1543998624,1543998833; uuid=f351320b3eeb4c939f58.1547436545.1.0.0; IJSESSIONID=162uyey7y7hnc6joppgc7cbv0; __utmc=74597006; ci3=1; client-id=f77b4a15-4378-4585-a088-c56138dee21c; __utma=74597006.484326599.1532933944.1547443187.1547445167.3; __utmz=74597006.1547445167.3.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; latlng=31.153185,121.502945,1547445169271; i_extend=C_b1Gimthomepagecategory11H__a; _lxsdk_s=1684b832404-66d-91c-dfb%7C%7C134"
        }

        yield scrapy.Request(url='http://meishi.meituan.com/i/api/channel/deal/list',
                        method='POST',
                        body = json.dumps(form_body),
                        cookies= cookies,
                        headers = headers,
                        dont_filter=True,
                        callback=self.parse_store
                 )


        # for cate in cateList:
        #     for area in areaList:
        #         scrapy.Request(url= 'http://meishi.meituan.com/i/api/channel/deal/list',
        #                        method='POST',
        #                        body = {},
        #                        callback=self.parse_store
        #         )


    def parse_store(self, response):
        data = response.body.decode()

        json_data = json.loads(data)


