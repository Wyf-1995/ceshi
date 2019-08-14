# coding:utf-8
from appium  import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = '112980c47d33'
desired_caps['appPackage'] = 'com.android.contacts'
desired_caps['appActivity'] = '.activities.PeopleActivity'


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

time.sleep(5)
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/miui.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ListView/android.view.ViewGroup[3]/android.widget.TextView[2]")
el1.click()

time.sleep(3)
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[5]/android.widget.FrameLayout")
el2.click()

time.sleep(3)
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout[1]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText")
el3.click()
el3.send_keys("beijing")

time.sleep(3)
el4 = driver.find_element_by_accessibility_id("确定")
el4.click()


