# coding:utf-8
from appium import webdriver
import time
import unittest

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['deviceName'] = '112980c47d33'
        desired_caps['appPackage'] = 'com.miui.calculator'
        desired_caps['appActivity'] = '.cal.CalculatorActivity'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(2)

    def test_01_something(self):
        add_2=self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        add_3.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add=self.driver.find_element_by_id("com.miui.calculator:id/btn_plus_s")
        add.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        add_3.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        sum=self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        sum.click()
        time.sleep(1)

        result=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/com.miui.support.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        act=result.get_attribute("text")
        exp="24,644"
        self.assertEqual(act, exp)
        time.sleep(1)

        clear=self.driver.find_element_by_accessibility_id(u"清除")
        clear.click()
        time.sleep(1)

    def test_02_something(self):
        add_2=self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_5 = self.driver.find_element_by_id("com.miui.calculator:id/btn_5_s")
        add_5.click()
        time.sleep(1)

        add_3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        add_3.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        chengfa=self.driver.find_element_by_accessibility_id(u"乘")
        chengfa.click()
        time.sleep(1)

        add_1 = self.driver.find_element_by_id("com.miui.calculator:id/btn_1_s")
        add_1.click()
        time.sleep(1)

        add_3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        add_3.click()
        time.sleep(1)

        add_6 = self.driver.find_element_by_id("com.miui.calculator:id/btn_6_s")
        add_6.click()
        time.sleep(1)

        add_6 = self.driver.find_element_by_id("com.miui.calculator:id/btn_6_s")
        add_6.click()
        time.sleep(1)

        sum=self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        sum.click()
        time.sleep(1)

        result=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/com.miui.support.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        act=result.get_attribute("text")
        exp="3,458,712"
        self.assertEqual(act, exp)
        time.sleep(1)

        clear = self.driver.find_element_by_accessibility_id(u"清除")
        clear.click()
        time.sleep(1)

    def test_03_something(self):
        add_2=self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_5 = self.driver.find_element_by_id("com.miui.calculator:id/btn_5_s")
        add_5.click()
        time.sleep(1)

        add_3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        add_3.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        chu=self.driver.find_element_by_accessibility_id(u"除")
        chu.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        add_3.click()
        time.sleep(1)

        add_5 = self.driver.find_element_by_id("com.miui.calculator:id/btn_5_s")
        add_5.click()
        time.sleep(1)

        add_6 = self.driver.find_element_by_id("com.miui.calculator:id/btn_6_s")
        add_6.click()
        time.sleep(1)

        sum=self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        sum.click()
        time.sleep(1)

        result=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/com.miui.support.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        act=result.get_attribute("text")
        exp="1.07470289"
        self.assertEqual(act, exp)
        time.sleep(1)

        clear = self.driver.find_element_by_accessibility_id(u"清除")
        clear.click()
        time.sleep(1)

    def test_04_something(self):
        add_9=self.driver.find_element_by_id("com.miui.calculator:id/btn_9_s")
        add_9.click()
        time.sleep(1)

        add_5 = self.driver.find_element_by_id("com.miui.calculator:id/btn_5_s")
        add_5.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_7 = self.driver.find_element_by_id("com.miui.calculator:id/btn_7_s")
        add_7.click()
        time.sleep(1)

        jian=self.driver.find_element_by_accessibility_id(u"减")
        jian.click()
        time.sleep(1)

        add_2 = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        add_2.click()
        time.sleep(1)

        add_3 = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        add_3.click()
        time.sleep(1)

        add_5 = self.driver.find_element_by_id("com.miui.calculator:id/btn_5_s")
        add_5.click()
        time.sleep(1)

        add_6 = self.driver.find_element_by_id("com.miui.calculator:id/btn_6_s")
        add_6.click()
        time.sleep(1)

        sum=self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        sum.click()
        time.sleep(1)

        result=self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/com.miui.support.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        act=result.get_attribute("text")
        exp="7,171"
        self.assertEqual(act, exp)
        time.sleep(1)

        clear = self.driver.find_element_by_accessibility_id(u"清除")
        clear.click()
        time.sleep(1)

if __name__ == '__main__':
    unittest.main()
