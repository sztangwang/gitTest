import os
import allure
import pytest
from excel import Excel
class TestClass:

    def setup_class(self):
        print(u"setup_class：所有用例执行之前")

    def teardown_class(self):
        print(u"teardown_class：所有用例结束后执行")

    @allure.feature('test_module_01')
    @allure.story('test_story_01')
    def test_case_01(self):
        """
        用例描述：Test case 01
        """
        assert 0 == 0

    datalist = Excel().read()
    @allure.feature('test_module_02')
    @allure.story('test_story_02')
    @pytest.mark.parametrize('param', datalist)
    def test_case_02(self,param):
        """
        用例描述：Test case 02
        """
        allure.attach('附件内容是： %s'% param)
        if param[1] != 'test4':
            Excel().write(int(param[0])+1,5,'Pass',"008000")
        else:
            Excel().write(int(param[0])+1, 5, 'Fail', "FF0000")
        assert param[1] != 'test4'


if __name__ == '__main__':
    pytest.main(['-s', 'pytest04.py','--alluredir', './report/xml'])
    os.system('pytest pytest04.py --alluredir=./tmp/my_allure_results --clean-alluredir')
    os.system('allure serve ./tmp/my_allure_results')
