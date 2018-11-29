# __author__: liqinsong
# data: 2018/11/20

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.douban.com")

driver.find_element_by_id("form_email").send_keys("1437050555@qq.com")
driver.find_element_by_id("form_password").send_keys("lqs123lqs")


time.sleep(5)
driver.find_element_by_class_name("bn-submit").click()

# 获取cookies
cookies = {i["name"]: i["value"] for i in driver.get_cookies()}
print(cookies)

driver.quit()
