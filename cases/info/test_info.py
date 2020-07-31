import pytest
from cases.common_api.common_function import UserInfo
from common.read_yaml import get_yaml_date
import os
import allure
from setting import base_dir
yml_path = os.path.join(base_dir, 'test_data', 'update_info.yml')
data = get_yaml_date(yml_path)
print(data['test_info_params'])


@allure.severity("blocker")
@allure.feature("个人信息模块")
@allure.story("修改个人信息接口用例")
@allure.title("用例描述,测试输入：{test_input}")
@pytest.mark.parametrize('test_input, expected',
                         data['test_info_params'],
                         ids=['修改个人信息sex=M，成功场景',
                              '修改个人信息sex=F，成功场景',
                              ]
                         )
def test_update(login_setup, test_input, expected):
    '''修改个人信息接口'''
    print('用例1')
    s = login_setup    # test_update(login_setup)这里调用的是fixture参数,它不是调用这个函数， 这里只是将fixture重新换个名称
    print(s.headers)
    # if not s.headers.get('Authorization', ''):
    #     pytest.skip('t未登录成功，跳过后面的用例')
    u = UserInfo(s)    # u = UserInfo(login_setup) 如果不重新换个名就这样写
    update = u.update_info(sex=test_input)        # 修改
    assert update['message'] == expected['message']
    assert update['code'] == expected['code']


@allure.feature("个人信息模块")
@pytest.mark.parametrize(data['test_eval_params'],
                         data['test_eval_values'])
def test_eval(test_input1, test_input2, expected):
    a = test_input1
    b = test_input2
    print('\na+b的值为:{}+{}={}'.format(eval(a), eval(b), expected))
    assert eval(a)+eval(b) == expected


@allure.feature("个人信息模块")
@allure.title("用例接口函数bug，跳过")
@pytest.mark.skip('跳过原因：该接口有bug')
def test_1():
    '''已经知道这个接口有bug'''
    print('已经知道这个接口有bug')


@allure.feature("个人信息模块")
@allure.title("自定义mark")
@pytest.mark.info                # info标签，名称任意取，>pytest -m info 可以执行打上标签的用例
def test_2(login_setup):
    print('info模块：自动化用例1')


