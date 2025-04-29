import pytest


class TestDemo:
    #创建数据
    data_list = ["xiaoming","xiaohong"]

    #参数化
    @pytest.mark.parametrize("name",data_list)
    def test_a(self,name):
        print("test_a")
        print(name)
        assert 1

if __name__ == '__main__':
    pytest.main(["pytest_one.py"])