# __author__: liqinsong
# data: 2018/11/14
import json
from parse_url import parse_url


class DouBanSpider(object):
    """豆瓣电视爬虫"""
    def __init__(self):
        self.start_url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start=0&count=18&loc_id=108288"

    def get_total_tvs(self):
        """ 获取总记录数据 """
        data = json.loads(parse_url(self.start_url))

        return int(data["total"])

    def run(self):
        # 1.遍历url列表 发送请求
        num = 0

        with open("AmericanTv.json", "w", encoding = "utf-8") as f:
            while num < self.get_total_tvs():

                url = "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start="+str(num)+"&count=18&loc_id=108288"

            # 2.获取返回数据
                data = parse_url(url)

            # 3.保存到本地
                json.dump(data, f, indent = 2, ensure_ascii = False)

                num = int(num) + 18
if __name__ == '__main__':
    douban = DouBanSpider()
    douban.run()
