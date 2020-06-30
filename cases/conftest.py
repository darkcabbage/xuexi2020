import pytest
import requests
from cases.common_function import login
import os


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


# （这一段是指从命令行传入的时候能够接收过来,实际上等于加到整个项目的配置上了）
# 添加命令行参数     parser是内置fixture       # default="xxx" 不传就自动调用默认值
def pytest_addoption(parser):
    parser.addoption("--cmdhost", action="store",
                     default="http://49.235.92.12:6009",
                     help="my option: host1 or host2"
                     )


# （接收过来之后，我们要让它在整个项目生效，autouse=True是指不需要引用也能自动生效）
@pytest.fixture(scope="session", autouse=True)
def host(request):
    '''获取命令行参数'''
    print("当前用例运行测试环境为：{}".format(request.config.getoption("--cmdhost")))
    os.environ["host"] = request.config.getoption("--cmdhost")   # 是指从request的配置也就是上面里面获取option


