import time

import pytest

# 创建fixture固件
# @pytest.fixture(scope="function", autouse=False, params=["成功", "失败"], ids=["success","fail"],name="sql")
# def exe_sql(request):
#     print("用例之前：执行SQL语句")
#     yield request.param  # 固件的返回值
#     print("用例之后：关闭数据库")

class Testapi():

    def test_login(self, exe_sql,exe_order):
        print(f"登录{exe_sql}")

    def test_register(self):
        print("注册")

    def test_add_user(self):
        print("增加用户")

    def test_del_user(self):
        print("删除用户")

    # def setup_class(self):
    #     print("每个类之前的操作：每个类只执行一次")
    #
    # def teardown_class(self):
    #     print("每个类之后的操作：每个类只执行一次")
    #
    # def setup_method(self):
    #     print("每个用例之前的操作：每个用例执行一次")
    #
    # def teardown_method(self):
    #     print("每个用例之后的操作：每个用例执行一次")
