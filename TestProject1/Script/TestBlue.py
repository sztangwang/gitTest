import time
import uiautomator2
import os


class TestBlue(object):

    def setup(self):
        """
        前置条件
        """
        with open('%s\log.txt' % os.getcwd(), 'wb+') as f:
            f.close()
        try:
            self.device = uiautomator2.connect()  # 连接usb设备
            print('手机usb设备连接成功')
        except:
            self.write_txt('手机usb设备连接失败')
            return False
        self.BLUE_NAME = 'MOZA R16-398D3BA2'  # 蓝牙设备名称
        return True

    def teardown(self):
        """
        后置条件
        用于断开蓝牙连接和关闭app
        :return:
        """
        print('点击断开连接......')
        try:
            self.device(description="断开连接").click()
            for i in range(15):
                if self.device.xpath("//*[@content-desc='跳过激活']").exists:
                    print('有弹出激活菜单，点击跳过激活.......')
                    self.device.xpath("//*[@content-desc='跳过激活']").click()
                    break
                else:
                    time.sleep(1)
            print('点击断开连接......')
            self.device(description="断开连接").click()
            self.device.app_stop('com.gudsen.mozapithouse')
            self.write_txt('蓝牙测试成功')
            print('蓝牙测试成功')
        except:
            self.write_txt('蓝牙后置条件退出断开测试异常')
            print('蓝牙后置条件退出断开测试异常')

    def blue_reconnect(self):
        self.device.xpath("//*[@content-desc='连接设备']").click()
        for i in range(30):
            tuple_coord = self.get_coord("//*[@content-desc='%s\n连接']" % self.BLUE_NAME)  # 获取xpath坐标位置
            if tuple_coord:
                print('已找到蓝牙设备： %s,根据蓝牙名称获取蓝牙连接按钮的坐标并点击........' % self.BLUE_NAME)
                self.device.click(tuple_coord[0] + 400, tuple_coord[1])  # 加400的意思是表示连接按钮的坐标位置

                break
            else:
                time.sleep(0.5)
                print('搜索蓝牙设备:%s..........' % self.BLUE_NAME)
            if i == 59:
                self.write_txt('测试失败，未搜索到蓝牙设备：%s' % self.BLUE_NAME)
                print('测试失败，未搜索到蓝牙设备：%s' % self.BLUE_NAME)
                return

        for i in range(20):  # 等待激活窗口
            if self.device.xpath("//*[@content-desc='跳过激活']").exists:
                print('有弹出激活菜单，点击跳过激活.......')
                self.device.xpath("//*[@content-desc='跳过激活']").click()
                break
            else:
                print('等待激活设备窗口')
                time.sleep(1)

        if self.device.xpath("//*[@content-desc='进入赛车']").exists:
            print('蓝牙设备连接成功')
            return True
        else:
            self.write_txt('蓝牙:%s连接失败' % self.BLUE_NAME)
            print('蓝牙:%s连接失败' % self.BLUE_NAME)
            return False

    def blue_connect(self):
        """
        连接 blue设备
        """
        print('启动app..........')
        self.device.app_start('com.gudsen.mozapithouse', 'com.gudsen.mozapithouse.MainActivity')
        for j in range(3): # 用于失败后重连
            if self.blue_reconnect():
                return True
            self.device.press('back') #按返回键重新进入刷新




    def blue_settings(self):
        """
        连接blue设备成功后进行参数设置test
        :return:
        """
        try:
            self.device.xpath("//*[@content-desc='进入赛车']").click()
            time.sleep(2)

            content = "最大限位角\n最大限位角\n同步转向角\n90°\n2000°"
            self.set_edit_text('1520', '1340', '//*[@content-desc="%s"]/android.widget.ImageView[1]' % content, content)

            content = "最大转向角\n最大转向角\n90°\n2000°"
            self.set_edit_text('760', '1340', '//*[@content-desc="%s"]/android.widget.ImageView[1]' % content, content)

            content = "路感灵敏度\n路感灵敏度\n0\n10"
            self.set_edit_text('3', '6', '//*[@content-desc="%s"]/android.widget.ImageView[1]' % content, content)
            self.device.press('back')
            return True
        except:
            self.write_txt('参数设置异常')
            return '参数设置失败'

    def get_coord(self, xpath):
        for elem in self.device.xpath(xpath).all():
            return elem.center()

    def write_txt(self, text):
        with open(r'%s\log.txt' % os.getcwd(), 'a', encoding='gbk') as f:
            f.write(text + "\n")
            f.close()

    def set_edit_text(self, default_text, text, xpath, content):
        """
        用于设置编辑框数据参数
        :param default_text: 默认值
        :param text: 正常值
        :param xpath: xpath路径
        :param content 控件用于滚动内容
        :return:
        """
        print('******************正在测试', xpath)
        self.device(scrollable=True).scroll.to(description=content)
        tuple_coord = self.get_coord(xpath)  # 获取xpath坐标位置
        self.device.click(tuple_coord[0] + 630, tuple_coord[1])  # 点击编辑框
        print('点击坐标:', tuple_coord)
        self.device.send_keys(default_text, clear=True)  # 先设置为默认值
        self.device.press('enter')
        time.sleep(1)
        self.device.press('back')  # 点击返回，目的是为了刷新，如果不刷新无法获取到最新的text内容，这样无法做判断
        time.sleep(1)
        self.device.xpath("//*[@content-desc='进入赛车']").click()
        time.sleep(1)
        self.device(scrollable=True).scroll.to(description=content)

        tuple_coord = self.get_coord(xpath)  # 获取xpath坐标位置
        self.device.click(tuple_coord[0] + 630, tuple_coord[1])  # 点击编辑框
        self.device.send_keys(text, clear=True)  # 先设置为正常值
        self.device.press('enter')

        for i in range(5):
            if self.device(text="%s, %s" % (int(text), int(default_text) * 100)).exists:
                time.sleep(1)
            else:
                return '参数设置成功'
            if i == 4:
                self.write_txt('参数设置失败%s' % xpath)
                return '参数设置失败'


if __name__ == '__main__':
    test_blue = TestBlue()
    result = test_blue.setup()  # 测试前置条件
    if result:
        result = test_blue.blue_connect()
    if result:
        result = test_blue.blue_settings()  # 参数设置
    if result:
        test_blue.teardown()  # 测试后置条件
