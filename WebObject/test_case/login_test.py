import os, sys, unittest
from selenium import webdriver
# sys.path.append('./models')
from models.driver import browser
# sys.path.append('./page_obj')
from page_obj.loginPage import Login, test_user_login, test_user_page
from page_obj.base import Page
from models.myunit import MyTest
from models.getScreen import insert_img
from time import sleep


class LoginTest(MyTest):


    username = 'username'
    password = 'password'

    def test_uname_err_login(self,username="username",password=password):
        test_user_login(self.driver,username,password)
        sleep(3)
        Login(self.driver).my_wait(20)
        errtext = Login(self.driver).err_text()

        insert_img(self.driver,'err_uname.png')
        assert(errtext == '不支持的登录类型'),'err提示出错!'
        
    def test_psword_err_login(self,username=username, password='123456789'):
        test_user_login(self.driver,username,password)
        sleep(4)
        Login(self.driver).my_wait(20)
        errtext = Login(self.driver).err_text()

        insert_img(self.driver,'err_psword.png')
        assert(errtext == '登录密码错误'),print("errtext:{}".format(errtext))

    def test_login(self, username=username, password=password):
        # driver =Login(self.driver)
        #调用登录函数
        test_user_login(self.driver,username,password)
        #调用base里面的隐形等待
        Login(self.driver).my_wait(20)
        test_user_page(self.driver)
        insert_img(self.driver,'登入.png')
        assert(self.driver.title == 'pythontest-豆果美食个人主页'), 'title不匹配，登录失败！'
        
if __name__ == '__main__':
    # main()
    unittest.main(verbosity=2)