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
    pytest.main(['run.py'])
    time.sleep(3)
    # 使用allure generate -o 命令将./allure_results目录下的临时报告生成到reports目录下变成html报告
    os.system("allure generate ./allure_results -o ./reports --clean")