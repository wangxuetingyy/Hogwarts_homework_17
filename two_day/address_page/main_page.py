#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/2/28 20:50
# ide： PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By

from Hogwarts_homework_17.two_day.address_page.address_page import AddressPage


class MainPage:
    def __init__(self):
        # 初始化，声明driver
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def goto_address(self):
        # 点击通讯录
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        # 把类初始化成对象
        return AddressPage(self.driver)