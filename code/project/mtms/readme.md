需求：
 抓取上海地区的美团美食商家信息：店铺名称、分类、地址、电话、人均消费、营业时间、评分、评价人数、经纬度
 
# 思路分析
### 起始url   http://meishi.meituan.com/i/?ci=10

#### 1.从起始url的请求中获取到所有分类,地区和uuidd等信息
#### 2.分析请求  通过上面的信息构造POST请求
#### 3.解析列表页,获取对应门店的url地址
#### 4.发送请求,解析门店详情页,提取数据

### 仍需解决问题 获取cookies 让之后的请求继续使用
#### 解决思路 从`i.meituan.com`中获取set-cookie的值组成cookies
