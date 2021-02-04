# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 0:07
# @Author  : Ting


#  编码格式
from typing import List


def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
    print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
