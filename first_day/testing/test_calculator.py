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


@pytest.fixture(params=get_data('add')[0], ids=get_data('add')[1])
def get_datas_add_fixture(request):
    return request.param


@pytest.fixture(params=get_data('div')[0], ids=get_data('div')[1])
def get_datas_div_fixture(request):
    return request.param


class TestCalc:
    # datas = get_data(
    add_datas = get_data('add')
    div_datas = get_data('div')

    # @pytest.mark.parametrize("a,b,result", add_datas[0], ids=add_datas[1])
    def test_add(self, get_instance, get_datas_add_fixture):
        f = get_datas_add_fixture
        assert f[2] == get_instance.add(f[0], f[1])

    # 浮点数
    @pytest.mark.parametrize("a,b,result", [(0.1, 0.1, 0.2), (0.1, 0.2, 0.3)])
    def test_add_float(self, get_instance, a, b, result):
        assert result == round(get_instance.add(a, b), 2)

    # @pytest.mark.parametrize("a,b,result", div_datas[0], ids=div_datas[1])
    def test_div(self, get_instance, get_datas_div_fixture):
        try:
            f = get_datas_div_fixture
            assert f[2] == get_instance.div(f[0], f[1])
        except ZeroDivisionError:
            print("分母不能为零")
    # 捕获异常
    # with pytest.raises(ZeroDivisionError):
    #     result = a/b
