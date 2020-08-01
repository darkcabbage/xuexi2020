import pytest
import requests
from cases.common_api.common_function import login


# 这种叫fixture参数，不叫函数
@pytest.fixture(scope='session')
def login_setup():
    '''先登录'''
    print('\n输入账号密码先登陆')
    s = requests.session()
    login(s)
    if not s.headers.get('Authorization', ''):
        pytest.skip('未登录成功，跳过后面的用例')
    yield s                # 相当于return s出来，因为定义的是session, 所以自动带上cookies，用例调用获取的是这个s
    print('后置操作')
    s.close()              # 关闭session


@pytest.fixture(scope='session')
def unlogin_setup():
    '''sql不登录'''
    print('''不登录1''')
    s = requests.session()
    yield s
    print('后置条件')


