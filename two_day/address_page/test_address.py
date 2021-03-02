#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/2/28 20:50
# ide： PyCharm
from Hogwarts_homework_17.two_day.address_page.main_page import MainPage


class TestAddress:
    def test_add_member(self):
        main = MainPage()
        # 首页-点击通讯录-添加成员
        main.goto_address().goto_add_member()
