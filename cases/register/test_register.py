import pytest
from cases.common_api.common_function import register
import allure


@allure.title("测试用例01_注册成功")
@allure.feature("注册模块")
def test_register_1(unlogin_setup, sql_fixture):
    '''测试用例01_注册成功'''
    s = unlogin_setup
    a = register(s)
    assert a.json()['code'] == 0
    assert a.json()['msg'] == '注册成功!'


@allure.title("测试用例02_重复注册")
@allure.feature("注册模块")
def test_register_2(unlogin_setup, sql_fixture):
    '''测试用例02_重复注册'''
    s = unlogin_setup
    a = register(s)         # 注册
    a2 = register(s)        # 重复注册
    assert a.json()['code'] == 0
    assert a.json()['msg'] == '注册成功!'
    assert a2.json()['code'] == 2000
    assert '用户已被注册' in a2.json()['msg']


if __name__ == '__main__':
    pytest.main('-s', 'test_register.py')


