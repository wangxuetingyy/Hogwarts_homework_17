# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 0:17
# @Author  : Ting
import pytest


@pytest.mark.parametrize('name', ["朱莉", "王利"])
def test_encode(name):
    print(name)

