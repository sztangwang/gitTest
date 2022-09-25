import pytest
import xlrd
import json


lines = []  # 创建空表用来存Excel每一行内容
worksheet = xlrd.open_workbook('../data/教管系统-测试用例V1.2.xls').sheet_by_index(2)
rows = worksheet.nrows  # 获取行数
for i in range(1, rows):
    line = worksheet.row_values(i)
    lines.append(line)


@pytest.fixture(params=lines)  # pytest工厂函数，默认方法级别
def init_x(request):
    return request.param  # 固定格式，每一次取出params的一个元素


class Test_x:
    def test_x(self, init_x):
        code = json.loads(init_x[6])  # 把第七列内容json格式的字符串转成字典格式
        code = code['code']  # 拿到code的值
        assert code != 0  # 断言是否通过