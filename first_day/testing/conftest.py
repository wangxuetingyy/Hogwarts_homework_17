# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 0:34
import pytest

from Hogwarts_homework_17.first_day.code.Calculator import Calculator


@pytest.fixture(scope='session')
def get_instance():
    print("--->开始计算<---")
    calc = Calculator()
    yield calc
    print("--->结束计算<---")