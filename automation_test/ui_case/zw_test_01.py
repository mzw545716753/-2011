from selenium import webdriver
import time

#设置配置文件路径  raw让字符显示原型
profire_configuration = r"C:\Users\sh01064\AppData\Roaming\Mozilla\Firefox\Profiles\kdowcsvy.default"

#加载配置文件
profire = webdriver.FirefoxProfile(profire_configuration)

#定义火狐类的对象
driver = webdriver.Firefox(profire)
time.sleep(3)
#打开网页
driver.get("https://www.baidu.com")
time.sleep(3)
#定位元素，输入内容
driver.find_element_by_id("kw").send_keys("毛志伟")
time.sleep(2)
#清空输入内容
driver.find_element_by_id("kw").clear()
#再次输入内容
time.sleep(3)
driver.find_element_by_id("kw").send_keys("毛逸恒")
#点击搜索按钮
time.sleep(3)
driver.find_element_by_id("su").click()

driver.implicitly_wait(10)

driver.find_element_by_id("su").click()

time.sleep(3)
# driver.get("http://www.sina.com")

#点击浏览器左箭头返回上一页面
# driver.back()
# time.sleep(3)
#
# #点击浏览器右箭头，切换下一页
# driver.forward()
# time.sleep(2)
# #刷新浏览器
# driver.refresh()
# time.sleep(3)
#
# #关闭当前浏览器页面
# driver.close()
# time.sleep(2)

driver.quit()