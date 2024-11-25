import allure
import pytest


@allure.epic("码尚教育自动化测试报告")
@allure.feature("用户管理模块")
class Testapi2():


    @allure.story("增加用户接口")
    @allure.title("验证成功增加用户")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.description("xxxx")
    @allure.link(url="http://www.baidu.com", name="接口访问链接")
    @allure.issue(url="http://www.baidu.com", name="bug链接")
    @allure.testcase(url="http:www.baidu.com", name="测试用例链接")
    # @allure.step("输入用户名和密码登录")
    def test_login(self):
        print(f"登录1111")
        # 多步骤一般用于 Web 自动化
        with allure.step("第1步：输入用户名"):
            with open("./tanhaowei.png", mode="rb") as f:
                allure.attach(body=f.read(),name="输入用户名截图",attachment_type = allure.attachment_type.PNG)
        with allure.step("第2步：xxxx"):
            with open("./tanhaowei.png", mode="rb") as f:
                allure.attach(body=f.read(),name="输入用户名截图",attachment_type = allure.attachment_type.PNG)
        with allure.step("第3步：xxxx"):
            with open("./tanhaowei.png", mode="rb") as f:
                allure.attach(body=f.read(),name="输入用户名截图",attachment_type = allure.attachment_type.PNG)
        # 接口自动化 （一般没有步骤，就只是发一个请求）
        allure.attach("get","请求方式",attachment_type=allure.attachment_type.TEXT)
        allure.attach("get","请求路径",attachment_type=allure.attachment_type.TEXT)
        allure.attach("get","请求参数",attachment_type=allure.attachment_type.TEXT)
        allure.attach("get","请求头",attachment_type=allure.attachment_type.TEXT)
        allure.attach("get","响应内容",attachment_type=allure.attachment_type.TEXT)

    @allure.story("增加用户接口")
    @allure.title("验证成功注册用户")
    def test_register(self):
        print("注册")



    # def test_add_user(self):
    #     allure.dynamic.epic("码尚教育自动化测试报告")
    #     allure.dynamic.feature("用户管理模块")
    #     allure.dynamic.story("增加用户接口")
    #     allure.dynamic.title("验证成功增加用户")
    #     print("增加用户")
    #
    # def test_del_user(self):
    #     allure.dynamic.epic("码尚教育自动化测试报告")
    #     allure.dynamic.feature("用户管理模块")
    #     allure.dynamic.story("增加用户接口")
    #     allure.dynamic.title("验证失败增加用户")
    #     print("删除用户")

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
