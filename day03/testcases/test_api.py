import allure
import pytest

from day03.commons.yaml_util import read_yaml


@allure.epic('项目名称：码尚教育金融项目接口自动化报告')
@allure.feature("模块名称：用户管理模块")
class Testapi3():
    yml_path = "./testcases/test_api.yaml"

    # @pytest.mark.parametrize("case_info",read_yaml(yml_path))
    # def test_login(self,case_info):
    #     print(f"登录：{case_info}")
    #
    # def test_register(self):
    #     print("注册")

    #用法一：
    @pytest.mark.parametrize("case_info",read_yaml(yml_path))
    def test_select_user1(self,case_info):
        print("-"*100)
        print(case_info)
        print(case_info["feature"])
        print(case_info["story"])
        print(case_info["title"])
        print(case_info["request"]["method"])
        print(case_info["request"]["url"])
        print(case_info["request"]["headers"])
        print(case_info["request"]["params"])
        print(case_info["validate"])
        print("-" * 100)


    # # 用法二：（不常用）
    # @pytest.mark.parametrize("name,age",[["百里",11],["北凡",12],["天秋",8]])
    # def test_select_user2(self,name,age):
    #    print(name,age)