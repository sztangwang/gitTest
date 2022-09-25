import pytest

class Test_pytest_class():

    def test_buy_now(self):
        print('test_buy_now')

    def test_buy_now2(self):
        print('test_buy_now2')

    def test_add_cart(self):
        print('test_add_cart')

    #测试自定义调用fixture函数方式1
    @pytest.mark.usefixtures('aa')
    def test_learn(self):
        print('装饰器方式调用fixtures函数')

    #测试自定义调用fixture函数方式1
    def test_learn2(self,aa):
        print('传参方式调用fixtures函数')


if __name__ == '__main__':
    pytest.main(["-s", "-v",'pytest02.py'])