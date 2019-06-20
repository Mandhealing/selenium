import unittest
from selenium import webdriver
from models.driver import browser
import os
#加载了browser和unittest测试框架
#有这个我们就不要每次都每次都建立 driver ，不需要每次都自己写setUp() 和tearDown(),只需要在需要执行的文件继承这个类
class MyTest(unittest.TestCase):
    def setUp(self):
        #创建一个chrome webdriver 实例
        self.driver = browser()
        self.driver.implicitly_wait(30)     
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()