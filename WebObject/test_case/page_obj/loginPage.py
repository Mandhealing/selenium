
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import os, sys
# sys.path.append('..')
from page_obj.base import Page
# import baseBB
class Login(Page):

    '''
    #登录页面模型
    '''
    
# 定位器
    a_loc = ('link text','登录')
    username_loc = (By.ID, "username")
    password_loc = (By.ID, "password")
    submit_loc = (By.ID, "login")
    css_loc =('css selector','a.headicon>img.wb100')
    err_loc =('id', 'err')
# Action
    def clicklogin(self):
        self.find_element(*self.a_loc).click()

    def type_username(self, username):

        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):

        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):

        self.find_element(*self.submit_loc).click()
        self.my_wait(30)

    def user_page(self):
        self.find_element(*self.css_loc).click()
        self.my_wait(10)

    def err_text(self):
        errtext = self.find_element(*self.err_loc).text
        # print (errtext)
        return errtext

    
    # def page_title(self):
    #     self.title
    

    def test_isfalse(self):
       logintest = self.find_element(*self.a_loc)
       assert logintest is False

    def isElementExist(self):
        try:
            self.find_element(*self.a_loc)
            return '登入失败'
        except:
            return print('登入成功')


def test_user_login(driver, username, password):
    """
    测试获取的用户名/密码是否可以登录
    """
    login_page = Login(driver)
    login_page.open()
    driver.implicitly_wait(30)
    login_page.clicklogin()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    driver.implicitly_wait(30)
    

def test_user_page(driver):
    Login(driver).user_page()