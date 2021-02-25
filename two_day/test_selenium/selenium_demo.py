#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/2/25 22:36 
# ide： PyCharm

import time
import json

from selenium import webdriver


class TestSelenium:
    def setup_method(self, method):
        # 浏览器复用
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.maximize_window()

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):
        # 获取cookie
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(10)
        cookies_list = self.driver.get_cookies()
        with open('data.txt', 'w', encoding='utf-8')as f:
            json.dump(cookies_list, f)

    def test_cookie_login(self):
        # 使用cookie登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open('data.txt', "r", encoding="utf-8") as f:
            cookies_list = json.load(f)
        for cookie in cookies_list:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(5)
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
