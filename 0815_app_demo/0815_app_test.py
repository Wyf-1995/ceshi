# coding:utf-8

from appium import webdriver
import time
import unittest

class MyTestCase(unittest.TestCase):

    @ classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = '112980c47d33'
        desired_caps['appPackage'] = 'com.miui.notes'
        desired_caps['appActivity'] = '.ui.NotesListActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(3)

    def test_01_something(self):
        ok_1 = self.driver.find_element_by_id("android:id/button1")
        ok_1.click()
        time.sleep(3)

        agree_1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.Button[2]")
        agree_1.click()
        time.sleep(3)

        add_1 = self.driver.find_element_by_accessibility_id(u"新建便签")
        add_1.click()
        time.sleep(3)

        input_1 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.EditText")
        input_1.click()
        input_1.send_keys(u"西门吹雪")
        time.sleep(3)

        over_1 = self.driver.find_element_by_accessibility_id(u"完成编辑")
        over_1.click()
        time.sleep(3)

        return_1 = self.driver.find_element_by_accessibility_id(u"返回")
        return_1.click()

        txt=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView")
        act=txt.get_attribute("text")
        exp = "西门吹雪"
        self.assertEqual(act,exp)


if __name__ == '__main__':
    unittest.main()
