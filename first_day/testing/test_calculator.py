#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/1/29 22:24 
# ide： PyCharm
import pytest
import yaml

from first_day.code.Calculator import Calculator


def get_data():
    with open("calc.yaml") as f:
        datas = yaml.safe_load(f)
    return datas['add']['datas'], datas['add']['ids']


class TestCalc:
    datas = get_data()

    def setup_class(self):
        print("\n开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("\n结束计算")

    @pytest.mark.parametrize("a,b,result", datas[0], ids=datas[1])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)

    @pytest.mark.parametrize("a,b,result", datas[0], ids=datas[1])
    def test_div(self, a, b, result):
        try:
            assert result == self.calc.div(a, b)
        except ZeroDivisionError:
            print("分母不能为零")
