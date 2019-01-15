import re
import json
from ast import literal_eval


with open("./ms.html", "r", encoding="utf-8") as f:
    data = f.read()

# print(data)

ret = re.findall("window._appState = (.*);</script>", data)[0]

json_data = json.loads(ret)


# print(json_data)
# print(json_data['navBarData']['categoryList'])  # 分类信息
areaList = json_data['navBarData']['areaList']  # 地区信息
# print(json_data['$meta']['uuid'])
quList = json_data['navBarData']['areaObj']



for key, value in quList.items():
    for val in value:
        if val.get("name") != '全部':
            print(val)


# import requests
#
# ret = requests.get("http://i.meituan.com")
# print(ret.cookies)


 # offset = 0
 #        limit = 15
 #
 #        while True:
 #            form_body = {
 #                "app": "",
 #                "areaId": 5,
 #                "cateId": 11,
 #                "deal_attr_23": "",
 #                "deal_attr_24": "",
 #                "deal_attr_25": "",
 #                "limit": limit,
 #                "lineId": 0,
 #                "offset": offset,
 #                "optimusCode": 10,
 #                "originUrl": "http://meishi.meituan.com/i/?ci=10",
 #                "partner": 126,
 #                "platform": 3,
 #                "poi_attr_20033": "",
 #                "poi_attr_20043": "",
 #                "riskLevel": 1,
 #                "sort": "default",
 #                "stationId": 0,
 #                "uuid": uuid,
 #                "version": "8.3.3"
 #            }
 #
 #            yield scrapy.Request(url='http://meishi.meituan.com/i/api/channel/deal/list',
 #                                 method='POST',
 #                                 body=json.dumps(form_body),
 #                                 headers=self.custom_settings['headers'],
 #                                 dont_filter=True,
 #                                 callback=self.parse_store
 #                                 )
 #
 #            if limit+offset > 400:
 #                print("提取完成")
 #                break
 #            else:
 #                print("加载第二页数据")
 #                offset += 15
