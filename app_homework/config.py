# coding:utf-8
class Conculater_Test():

    def __init__(self,driver):

        self.driver=driver
    @property
    def input_1(self):
        element=self.driver.find_element_by_id("com.miui.calculator:id/btn_1_s")
        return element

    @property
    def input_2(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_2_s")
        return element

    @property
    def input_3(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_3_s")
        return element

    @property
    def input_4(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_4_s")
        return element

    @property
    def input_5(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_5_s")
        return element

    @property
    def input_6(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_6_s")
        return element

    @property
    def input_7(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_7_s")
        return element

    @property
    def input_8(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_8_s")
        return element

    @property
    def input_9(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_9_s")
        return element

    @property
    def input_0(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_0_s")
        return element

    @property
    def plus(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_plus_s")
        return element

    @property
    def minus(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_minus_s")
        return element

    @property
    def mul(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_mul_s")
        return element

    @property
    def div(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_div_s")
        return element

    @property
    def equal(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_equal_s")
        return element

    @property
    def btn_c(self):
        element = self.driver.find_element_by_id("com.miui.calculator:id/btn_c_s")
        return element

    @property
    def result(self):
        element = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/com.miui.support.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.HorizontalScrollView[3]/android.widget.LinearLayout/android.widget.TextView[2]")
        return element





