#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/3/25 22:43
# ide： PyCharm
import requests


class TestAddress:
    def setup(self):
        self.token = self.get_access_token()

    # 获取access_token
    def get_access_token(self):
        r = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8183a70d2b88f6a5&corpsecret=3QVfp4GGO4aiY95ZR3Y36VBz2Uj7VDg1M9b4Re3MhVc")
        token = r.json()['access_token']
        return token

    # 读取成员
    def test_get_member(self):
        user_id = "xiaoying"
        get_member = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid={user_id}")
        print(get_member.json())

    # 创建成员
    def test_create_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        data = {
            "userid": "balabla",
            "name": "小魔仙",
            "mobile": "+86 13700070007",
            "department": [1]}
        create_member = requests.post(url, json=data)
        print(create_member.json())

    # 更新成员
    def test_update_member(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        data = {
            "userid": "balabla",
            "name": "小魔仙A",
            }
        update_member = requests.post(url, json=data)
        print(update_member.json())

    # 删除成员
    def test_delete_member(self):
        user_id = "balabla"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={user_id}"
        data = {
            "userid": "balabla"
            }
        delete_member = requests.post(url, json=data)
        print(delete_member.json())
