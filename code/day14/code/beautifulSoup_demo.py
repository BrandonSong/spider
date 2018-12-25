# __author__: liqinsong
# data: 2018/12/16

from bs4 import BeautifulSoup


html_str = """
<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46401&keywords=&tid=0&lid=0">TEG13-安全策略后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-12-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46395&keywords=&tid=0&lid=0">29313-PCG财务分析经理（北京）</a></td>
					<td>职能类</td>
					<td>1</td>
					<td>北京</td>
					<td>2018-12-16</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46397&keywords=&tid=0&lid=0">18432-金融产品项目经理</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-12-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46398&keywords=&tid=0&lid=0">25928-虚拟人研究高级工程师</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>美国</td>
					<td>2018-12-16</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46399&keywords=&tid=0&lid=0">25928-计算图形/视觉/动画高级算法工程师</a></td>
					<td>技术类</td>
					<td>3</td>
					<td>美国</td>
					<td>2018-12-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46400&keywords=&tid=0&lid=0">18796-H5开发工程师(深圳)</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-12-16</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46392&keywords=&tid=0&lid=0">PCG10-Android客户端开发工程师（成都）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>成都</td>
					<td>2018-12-16</td>
		    	</tr>
		        <tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46393&keywords=&tid=0&lid=0">S2-TEG财务分析经理（深圳）</a></td>
					<td>职能类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-12-16</td>
		    	</tr>
		    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46394&keywords=&tid=0&lid=0">PCG04-外包管理员（深圳）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-12-16</td>
		    	</tr>
		    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=46396&keywords=&tid=0&lid=0">18425-测试开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2018-12-16</td>
		    	</tr>
		    </table>
"""

soup = BeautifulSoup(html_str, "lxml")
# 使用beautifulsoup来完成如下需求
# 1.获取所有tr标签
# trs = soup.find_all('tr')
# for tr in trs:
#     print(tr)
#     print("="*30)

# 2.获取第二个tr标签
# limit指定最多获取几个元素
# tr = soup.find_all('tr', limit = 2)[1]
# print(tr)


# 3.获取所有class等于even的tr标签
# trs = soup.find_all('tr', attrs = {'class':'even'})
# for tr in trs:
#     print(tr)
#     print('*'*30)

# 4.获取所有id等于test,class也等于test的a标签
# aList = soup.find_all('a', id='test', class_='test')
# for a in aList:
#     print(a)

# 5.获取所有a标签的href属性
# hrefs = soup.find_all('a')
# for href in hrefs:
#     # 1.通过下标来操作获取属性
#     h = href["href"]
#     # 2.通过attrs属性的方式
#     h1 = href.attrs['href']
#     print(h, h1)

# 6.获取所有职位信息(纯文本)
# trs = soup.find_all('tr')[1:]
# for tr in trs:
#     tds = tr.find_all('td')
#     # 获取某个标签下的文本内容
#     title = tds[0].string
#     print(title)