#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/2/28 20:50
# ide： PyCharm
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    # 传进driver,方便其它函数引用
    def __init__(self, driver):
        self.driver = driver

    def goto_add_member(self):
        """
        不可交互
        1、元素被遮挡，元素前面还有其它不可见元素
        2、元素有多个，需要人工选中合适的元素
        :return:
        """

        # 闭包
        def wait_name(driver):
            vas = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn js_add_member']")
            # print(len(vas))
            vas[-1].click()
            vas = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(vas) > 0
        WebDriverWait(self.driver, 10).until(wait_name)
        # 录入姓名、账号、手机号，保存按钮
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("周生生")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("zhoushengsheng1")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("15789890001")
        self.driver.find_element(By.XPATH, "//*[@class='qui_btn ww_btn js_btn_save']").click()
