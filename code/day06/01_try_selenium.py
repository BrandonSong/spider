# __author__: liqinsong
# data: 2018/11/19

from selenium import webdriver
import time

driver = webdriver.PhantomJS(r"D:\tools\phantomjs-2.1.1-windows\bin\phantomjs.exe")

driver.get("https://www.baidu.com")

# 设置窗口大小
# driver.set_window_size(1920, 1080)

# 元素定位的方法并输入内容
# driver.find_element_by_id("kw").send_keys("python")

# 点击按钮
# driver.find_element_by_id("su").click()

# driver获取cookie
# cookies = driver.get_cookies()
# cookies = {i["name"]: i["value"] for i in cookies}
# print(cookies)

# driver获取HTML字符串
print(driver.page_source)  # 浏览器中elements的内容


# time.sleep(3)


# 退出浏览器
driver.quit()
