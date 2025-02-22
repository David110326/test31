import pytest


class TestDemo:
    #创建数据
    data_list = [("xiaoming","24353"),("xiaohong","123456")]

    #参数化
    @pytest.mark.parametrize(("name","password"),data_list)
    def test_a(self,name,password):
        print("test_a")
        print(name,password)
        assert 1

if __name__ == '__main__':
    pytest.main(["pytest_two.py"])