from pickle import FALSE

import pytest


# 创建fixture固件
@pytest.fixture(scope="function", autouse=False)
def exe_sql():
    print("---1111111111111111111用例之前：执行SQL语句----")
    yield
    print("---111111111111用例之后：关闭数据库---")

#创建fixture固件
@pytest.fixture(scope="function",autouse=False)
def exe_order():
    print("11111111111用例之前：订单之前")
    yield
    print("1111111111用例之后：订单之后")
