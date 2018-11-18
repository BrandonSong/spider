# __author__: liqinsong
# data: 2018/11/16


class TieBaSpider(object):
    def __init__(self):
        pass

    def run(self):
        """实现主要逻辑"""
        # 1.start_url
        # 2.发送请求,获取响应
        # 3.提取数据,提取下一页的url地址
            # 3.1提取列表页的url地址和标题
            # 3.2请求列表页的url地址,获取详情页的第一页
            # 3.3提取详情页第一页的图片,提取下一页的地址
            # 3.4请求详情页下一页的地址,重复3.2-3.4步
        # 4.保存数据
        # 5.请求下一页的url地址,进入2-5步