from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


#设置配置文件路径  raw让字符显示原型
profire_configuration = r"C:\Users\sh01064\AppData\Roaming\Mozilla\Firefox\Profiles\kdowcsvy.default"

#加载配置文件
profire = webdriver.FirefoxProfile(profire_configuration)

driver = webdriver.Firefox(profire)

driver_url = "https://www.baidu.com"

driver.implicitly_wait(10)

driver.get(driver_url)
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='u1']/a[9]").click()
time.sleep(3)
driver.find_element_by_link_text("搜索设置").click()
time.sleep(3)
dj = driver.find_element_by_id("nr")
time.sleep(3) 
#driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
Select(dj).select_by_index(1)
time.sleep(3)
dj.click()
time.sleep(3)
driver.quit()
