# coding:utf-8
from appium import webdriver
import time
import unittest
from app_homework.config import Conculater_Test

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
        cls.way = Conculater_Test(cls.driver)
        time.sleep(2)

    def test_01_add_1345_3456(self):
        self.way.input_1.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.plus.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.input_6.click()
        self.way.equal.click()

        time.sleep(1)
        act=self.way.result.text
        exp="4,801"
        self.assertEqual(act,exp)

        self.way.btn_c.click()
        time.sleep(1)

    def test_02_minus_1345_3456(self):
        self.way.input_1.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.minus.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.input_6.click()
        self.way.equal.click()

        time.sleep(1)
        act = self.way.result.text
        exp = "-2,111"
        self.assertEqual(act, exp)

        self.way.btn_c.click()
        time.sleep(1)

    def test_03_mul_1345_3456(self):
        self.way.input_1.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.mul.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.input_6.click()
        self.way.equal.click()

        time.sleep(1)
        act = self.way.result.text
        exp = "4,648,320"
        self.assertEqual(act, exp)

        self.way.btn_c.click()
        time.sleep(1)


    def test_04_div_1345_3456(self):
        self.way.input_1.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.div.click()
        self.way.input_3.click()
        self.way.input_4.click()
        self.way.input_5.click()
        self.way.input_6.click()
        self.way.equal.click()

        time.sleep(1)
        act = self.way.result.text
        exp = "0.389178241"
        self.assertIn(exp, act)

        self.way.btn_c.click()
        time.sleep(1)



if __name__ == '__main__':
    unittest.main()
