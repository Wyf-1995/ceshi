# coding:utf-8
from appium  import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = '112980c47d33'
desired_caps['appPackage'] = 'com.miui.notes'
desired_caps['appActivity'] = '.ui.NotesListActivity'
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
el1 = driver.find_element_by_id("android:id/button1")
el1.click()
time.sleep(3)
el2 = driver.find_element_by_id("android:id/button1")
el2.click()
time.sleep(3)
el3 = driver.find_element_by_accessibility_id("新建便签")
el3.click()
time.sleep(3)
el4 = driver.find_element_by_id("com.miui.notes:id/rich_editor")
el4.click()
el4.send_keys("辉远科技")
time.sleep(3)
el5 = driver.find_element_by_accessibility_id("完成编辑")
el5.click()
time.sleep(3)
el6 = driver.find_element_by_accessibility_id("返回")
el6.click()



