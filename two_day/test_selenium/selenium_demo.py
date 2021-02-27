#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/2/25 22:36 
# ide： PyCharm

import time
import json

from selenium import webdriver


class TestSelenium:
    def setup_method(self):
        """
        一、打开浏览器 chrome --remote-debugging-port=9222
        # 二、python复用浏览器
        :return:
        """
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_get_cookie(self):
        """
        登录后,获取cookie
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookies_list = self.driver.get_cookies()
        with open('data.txt', 'w', encoding='utf-8')as f:
            json.dump(cookies_list, f)  # 传入流

    def test_login_cookie(self):
        """
        使用cookie登录
        :return:
        """
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open('data.txt', "r", encoding="utf-8") as f:
            cookies_list = json.load(f)
        for cookie in cookies_list:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        time.sleep(5)

