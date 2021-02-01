#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： Ting
# datetime： 2021/1/29 22:24 
# ide： PyCharm
import pytest
import yaml

from first_day.code.Calculator import Calculator


def get_data(name):
    with open("calc.yaml") as f:
        all_datas = yaml.safe_load(f)
        datas = all_datas[name]['datas']
        ids = all_datas[name]['ids']
    return datas, ids


class TestCalc:
    # datas = get_data(
    add_datas = get_data('add')
    div_datas = get_data('div')

    def setup_class(self):
        print("\n开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("\n结束计算")

    @pytest.mark.parametrize("a,b,result", add_datas[0], ids=add_datas[1])
    def test_add(self, a, b, result):
        assert result == self.calc.add(a, b)

    # 浮点数
    # 或者 from decimal import Decimal
    @pytest.mark.parametrize("a,b,result", [(0.1, 0.1, 0.2), (0.1, 0.2, 0.3)])
    def test_add_float(self, a, b, result):
        assert result == round(self.calc.add(a, b), 2)

    @pytest.mark.parametrize("a,b,result", div_datas[0], ids=div_datas[1])
    def test_div(self, a, b, result):
        try:
            assert result == self.calc.div(a, b)
        except ZeroDivisionError:
            print("分母不能为零")
        # 捕获异常
        # with pytest.raises(ZeroDivisionError):
        #     result = a/b
