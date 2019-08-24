#  coding:utf-8
import unittest
from appium import webdriver
import time
from App_scrip.wukong import Wukong_Test
from App_scrip import config


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        desired_caps = {}
        desired_caps['platformName'] = config.platformName
        desired_caps['platformVersion'] = config.platformVersion
        desired_caps['automationName'] = config.automationName
        desired_caps['deviceName'] = config.deviceName
        desired_caps['appPackage'] = config.appPackage
        desired_caps['appActivity'] = config.appActivity
        desired_caps['unicodeKeyboard'] = config.unicodeKeyboard
        desired_caps['resetKeyboard'] = config.resetKeyboard
        desired_caps['noReset'] = config.noReset

        url="http://%s:%s/wd/hub"%(config.Remote_ip,config.Remote_post)
        cls.driver = webdriver.Remote(url, desired_caps)
        cls.way = Wukong_Test(cls.driver)
        time.sleep(5)

    # 登录
    # def test_01_login(self):
    #     self.way.user_name.click()
    #     self.way.user_name.send_keys(u'18062502916')
    #     time.sleep(1)
    #
    #     self.way.password.click()
    #     self.way.password.send_keys(u'123456')
    #     time.sleep(1)
    #
    #     self.way.login.click()
    #     time.sleep(1)
    #
    #     act = self.way.title_wukongCRM.text
    #     exp = "悟空CRM"
    #     self.assertEqual(act, exp)

    # 跳转我的页面
    def test_02_Jump_My(self):
        self.way.My_button.click()
        time.sleep(1)

        act=self.way.title_My.text
        exp="我的"
        self.assertEqual(act, exp)

    # 跳转我的个人信息
    # def test_03_Jump_My_information(self):
    #     self.way.My_photo.click()
    #     time.sleep(1)
    #
    #     act=self.way.title_information.text
    #     exp="个人信息"
    #     self.assertEqual(act, exp)
    #
    #     self.way.return_My.click()
    #     time.sleep(1)
    #
    # # 跳转企业通讯录
    # def test_04_Jump_phone_list(self):
    #     self.way.phone_list.click()
    #     time.sleep(1)
    #
    #     self.way.tel_num.click()
    #     time.sleep(1)
    #
    #     act=self.way.Jump_call.text
    #     exp="通话"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #
    # # 拨打企业通讯录中的电话
    # def test_05_service_phone(self):
    #     self.way.only_service.click()
    #     time.sleep(1)
    #
    #     self.way.service_sure.click()
    #     time.sleep(1)
    #
    #     act=self.way.service_phone.text
    #     exp="400 081 2558"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    # # 我的待办
    # def test_06_wait_solve(self):
    #     self.way.wait_my_solve.click()
    #     time.sleep(1)
    #
    #     act=self.way.title_wait_solve.text
    #     exp="待办事项"
    #     self.assertEqual(act, exp)
    #
    #     self.way.My_button.click()
    #     time.sleep(1)
    #
    # # 我的待办（拒绝）
    # def test_07_My_wait_solve_refuse(self):
    #     self.way.My_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.Enter_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.refuse_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.reason_refuse.click()
    #     self.way.reason_refuse.send_keys(u"拒绝")
    #     time.sleep(1)
    #
    #     self.way.save_reason.click()
    #     time.sleep(0.5)
    #
    #     self.way.save_reason_sure.click()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.way.solve.click()
    #     time.sleep(1)
    #
    #     act=self.way.status_refuse.text
    #     exp="普通审批-拒绝"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #
    # # 我的待办（同意）
    # def test_08_My_wait_solve_agree(self):
    #     self.way.My_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.Enter_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.agree_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.save_agree.click()
    #     time.sleep(1)
    #
    #     self.way.sure_agree.click()
    #     time.sleep(1)
    #
    #     act=self.way.status_agree.text
    #     exp="通过"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    # # 我的待办（撤回）
    # def test_09_My_wait_solve_return(self):
    #     self.way.My_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.Enter_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.return_wait_solve.click()
    #     time.sleep(1)
    #
    #     self.way.return_send_keys.click()
    #     self.way.return_send_keys.send_keys(u"撤回")
    #     time.sleep(1)
    #
    #     self.way.save_return.click()
    #     time.sleep(0.5)
    #
    #     self.way.sure_save_return.click()
    #     time.sleep(1)
    #
    #     act=self.way.result_return.text
    #     exp="撤回"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    # # 跳转系统设置
    # def test_10_sys_setting(self):
    #     self.way.sys_setting.click()
    #     time.sleep(1)
    #
    #     self.way.Relevant_wukong.click()
    #     time.sleep(1)
    #
    #     act=self.way.setting_result_1.text
    #     exp="设置"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    # # 系统设置打电话
    # def test_11_sys_setting(self):
    #     self.way.sys_setting.click()
    #     time.sleep(1)
    #
    #     self.way.Relevant_wukong.click()
    #     time.sleep(1)
    #
    #     self.way.setting_tel.click()
    #     time.sleep(1)
    #
    #     act=self.way.setting_phone.text
    #     exp="400 081 2558"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    # # 跳我的日志
    # def test_12_My_Journal(self):
    #     self.way.My_Journal.click()
    #     time.sleep(1)
    #
    #     act=self.way.title_Journal.text
    #     exp="日志"
    #     self.assertEqual(act, exp)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    # # 我的日志——评论
    # def test_13_My_Journal_comment(self):
    #     self.way.My_Journal.click()
    #     time.sleep(2)
    #
    #     self.way.choice_Journal.click()
    #     time.sleep(2)
    #
    #     self.way.choice_input.click()
    #     self.way.choice_input.send_keys(u"吴彦祖")
    #     time.sleep(2)
    #
    #     self.way.send_input.click()
    #     time.sleep(2)
    #
    #     act=self.way.result_input.text
    #     exp="吴彦祖"
    #     self.assertIn(exp,act)
    #
    #     self.driver.back()
    #     time.sleep(1)
    #
    #     self.driver.back()
    #     time.sleep(2)

    # 我的日志——删除
    def test_14_My_Journal_delete(self):
        self.way.My_Journal.click()
        time.sleep(1)

        self.way.choice_Journal.click()
        time.sleep(1)

        self.way.choice_more.click()
        time.sleep(1)

        self.way.choice_delete.click()
        time.sleep(1)

        self.way.sure_delete.click()
        time.sleep(1)

        act=self.way.result_delete.text
        exp="日志"
        self.assertEqual(act,exp)

        self.driver.back()
        time.sleep(1)

    # 收到的日志
    def test_15_My_Journal_recevied(self):
        self.way.recevied_Journal.click()
        time.sleep(3)

        act=self.way.result_recevied.text
        exp="我收到的"
        self.assertEqual(act,exp)

        self.driver.back()
        time.sleep(1)

    # 我发起的审批
    def test_16_My_launch(self):
        self.way.My_launch.click()
        time.sleep(1)

        act=self.way.result_launch.text
        exp="我发起的"
        self.assertEqual(act,exp)

        self.driver.back()
        time.sleep(1)

    def test_17_company_list(self):
        self.way.phone_list.click()
        time.sleep(1)

        act=self.way.result_company.text
        exp="公司通讯录"
        self.assertEqual(act,exp)

        self.driver.back()
        time.sleep(1)






























if __name__ == '__main__':
    unittest.main()
