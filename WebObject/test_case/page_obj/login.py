from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class Page(object):

    '''
    基础类，用于页面对象类的继承
    '''
    login_url = 'https://www.douguo.com'
    url = '/'

    def __init__(self, selenium_driver, base_url=login_url):

        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30

    def on_page(self):

        return self.driver.current_url == (self.base_url + self.url)

    def _open(self, url):

        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(), 'Did not land on %s' % url

    def open(self):

        self._open(self.url)

    def find_element(self, *loc):

        return self.driver.find_element(*loc)


class LoginPage(Page):

    '''
    #登录页面模型
    '''
    
# 定位器
    a_loc = ('link text','登录')
    username_loc = (By.ID, "username")
    password_loc = (By.ID, "password")
    submit_loc = (By.ID, "login")
    css_loc =('css selector','a.headicon>img.wb100')
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
        self.driver.implicitly_wait(30)

    def perpage(self):
        self.find_element(*self.css_loc).click()
        self.driver.implicitly_wait(10)
    
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
    login_page = LoginPage(driver)
    login_page.open()
    driver.implicitly_wait(30)
    login_page.clicklogin()
    login_page.type_username(username)
    login_page.type_password(password)
    login_page.submit()
    # login_page.perpage()
    # title = driver.title
    # return title
    # login_page.isElementExist()
    


def main():
    try:
        driver = webdriver.Chrome()
        username = 'username'
        password = 'password'
        driver.maximize_window()
        test_user_login(driver, username, password)
        sleep(3)
        driver.implicitly_wait(20)
        assert(driver.title == 'pythontest-豆果美食个人主页'),'title不匹配，登录失败！'
        # assert(driver.find_element('link text','登录').text),'登入成功！'
        # text = driver.find_element_by_xpath("//span[@id='spnUid']").text
        # assert(text == 'username@126.com'), "用户名称不匹配，登录失败!"
        
    finally:
        # 关闭浏览器窗口
        # pass
        driver.close()

if __name__ == '__main__':
    main()
