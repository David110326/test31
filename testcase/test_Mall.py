# #登录测试用例
# #登录
# #1、导入包
# import json
# from selenium.webdriver.chrome import webdriver
# import pytest
# import requests
# #2、定义登录方法
# from utils.RequestUtil import requests_get
# from utils.RequestUtil import Request
# from config.Conf import ConfigYaml
#
# def test_login():
# #3、定义测试数据
#     conf_y = ConfigYaml()
#     url = conf_y.get_conf_url()
#
#     # url = "http://httpbin.org/get"
#     # data = {"username":"python","password":"12345678"}
# # 发送POST请求
# #     r = requests.get(url)
#     #r = requests_get(url)
#     request = Request()
#     r = request.get(url,headers=None)
#     # print(r)
#     print(r["code"])
#     for item in r["body"]:
#         print(item+":",r["body"][item])
#     for item in r["body"]["headers"]:
#         print(item+":",r["body"]["headers"][item])
#
#
# #5、输出结果
#     # print(r.json()) #r.text
#     # print(r["code"])
#     # print(r["body"])
#
# def test_check():
#     url = "http://httpbin.org/post"
#     data = {
#         "dep_id":"T01",
#         "dep_name":"Test university",
#         "master_name":"'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip}",
#         "slogan":"Here is Slogan"
#     }
#     # r=requests.post(url,data=data)
#     # #将python对象转换json字符串（格式化返回）
#     # print(r)
#     # print(r.status_code)
#     # result = json.dumps(r.json(), indent=2, ensure_ascii=False)
#     # print(result)
#     request = Request()
#     r =request.post(url,json= data)
#     print(r)
#
# if __name__ == '__main__':
#     #test_login()
#     #check()
#     pytest.main(["-s"])

import os
import time

import allure



import pytest

from datetime import datetime
@allure.feature("用户管理")
@allure.story("用户登录")
def test_1():
    print("test1")
    print("test case 1:",datetime.now())

def test_2():
    print("test2")
    print("test case 2:",datetime.now())

def test_3():
    print("test3")
    print("test case 1:",datetime.now())

if __name__ == '__main__':
    # pytest.main(["allure_demo.py"])
    # 打开实时输出，Captrue Log只捕获sys.out，sys.err
    pytest.main(['test_Mall.py'])
    time.sleep(3)
    # 使用allure generate -o 命令将./allure_results目录下的临时报告生成到reports目录下变成html报告
    os.system("allure generate ./allure_results -o ./reports --clean")