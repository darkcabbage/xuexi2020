import pytest
from common.connect_mysql import execute_sql


@pytest.fixture(scope='function')
def sql_fixture():
    '''执行sql,删除注册'''
    delete_sql = "delete from auth_user where username = 'testadmin';"
    execute_sql(delete_sql)
    yield
    print('后置清理数据操作')