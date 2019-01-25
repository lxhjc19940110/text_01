from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import base64
def setup_class(self):

    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '127.0.0.1:4723'
    # app信息
    # desired_caps['app'] = 'D:\pyth\com.example.corel.calc_2.1.1023_11.apk'

    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    desired_caps['unicodekeyboard'] = True
    desired_caps['resetkeyboard'] = True
        # 声明手机驱动对象 自启动启动参数中指定的APP post接口  创建session
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

def teardown_class(self):
    self.driver.quit()

def test_abc_01(self):
    save = self.driver.find_element_by_xpath("//*[contains(@text,'存储')]")
    more = self.driver.find_element_by_xpath("//*[contains(@text,'更多')]")
    self.driver.drag_and_drop(save,more)