## Python + selenium + unittest(Page Object)


### 为什么搭建这个框架？
- 第一个我在网上找了一些资料介绍这个框架的，但是大部分都有问题，就算改了代码还是有一些问题
- 第二个就是为了招工作学习了搭建自动化框架
- 第三个就是以后需要用的时候，方便我稍微修改一下就可以立马用


### 什么是Page Object
>Page Object模式，创建一个对象来对应页面的一个应用。因此，我们可以为每个页面定义一个类，并为每个页面的属性和操作构建模型。这就相当于在测试脚本和被测的页面功能中分离出一层，屏蔽了定位器、底层处理元素的方法和业务逻辑，取而代之的是，Page Object会提供一系列的API来处理页面功能
上面我是从一些书上找的，大家可以看看，好处就是方便分模写测试用例，尽量减少重复代码，同时也易于维护代码

### 前置知识和环境安装
前置知识:
1.需要入门级Python知识，大家可以去实验楼操作学习
2.看一下Selenium API 文档
环境:
安装Python3.7 和selenium2
下载对应的webdriver，放到浏览器安装目录下

### 项目目录结构
```
#这个目录也是参考别人的
WebAuto/
    ├─data/                    #如果数据驱动，数据文件就存放在这里
    ├─report/                  #生成html报告的目录
    │  └─image/                #存放截图的目录
    └─test_case/               #放测试用例的目录
        ├─models/              #一些公共类
        │  ├─driver.py         #webdriver
        │  ├─getScreen.py      #截图
        │  ├─myunit.py         #unittest测试框架，引入了driver
        │  └─pilimage.py       #简单的验证码识别
        ├─page_obj/            #页面类
        │  ├─base.py           #总的类，所有页面都需要继承
        │  ├─login.py          #没有Page Object设计的代码
        │  ├─loginPage.py      #登入页面类需要的操作，我把定位也封装在这里了
        ├─login_test.py        #调用loginPage,设计登入页面业务场景
        └─run_test_all.py      #执行测试用例和生成测试报告
    └─HTMLTestRunner.py        #修改后的支持python3.7
```


### 代码分离和引用

#### - 代码不分离
在没有Page Object设计模式下，我们一般怎么写？比如下面：
```python
#我们也不怎么去封装函数
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

class Page(object):

    '''
    从上到下的执行的测试用例
    '''
    def login(driver,username, password):
        url = 'https://www.douguo.com'
        # 定位器
        a_loc = ('link text','登录')
        username_loc = (By.ID, "username")
        password_loc = (By.ID, "password")
        submit_loc = (By.ID, "login")
        driver = driver
        driver.get(url)
        driver.implicitly_wait(30)
        driver.find_element(*a_loc).click()
        driver.implicitly_wait(30)
        usName = driver.find_element(*username_loc)
        usName.clear()
        usName.send_keys(username)
        psWord = driver.find_element(*password_loc)
        psWord.clear()
        psWord.send_keys(password)
        sleep(3)
        submit = driver.find_element(*submit_loc)
        submit.click()
        driver.implicitly_wait(30)
        sleep(3)

if __name__ == '__main__':
    try:
        username = 'username'
        password = 'password'
        css_loc =('css selector','a.headicon>img.wb100')
        driver = webdriver.Chrome()
        driver.maximize_window()
        Page.login(driver, username, password)
        driver.find_element(*css_loc).click()
        assert(driver.title == 'pythontest-豆果美食个人主页'),'title不匹配，登录失败！'
   
    finally:
        pass
        # driver.close()
```
如果项目项目很大，各个测试人员都这样写测试用例脚本，项目有所变动，就不好维护代码，代码重复性也很高，所以我们需要有设计模式

#### - 代码分离和引用
下面我们通过用Page Object设计模式来实现:
```python
#这里讲下怎么分离和引用的
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import unittest

#创建base脚本类(base.py)
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

#创建登录页面脚本类(loginPage.py)
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
    

#登入业务场景脚本(login_test.py)
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
        
    finally:
        # 关闭浏览器窗口
        # pass
        driver.close()

if __name__ == '__main__':
    main()
```
#### - 脚本之间关系
大致说下脚本之间的关系
page_obj页面可以建新的page页面
所有的*Page.py都继承base的page类
业务场景测试用例继承myunit的类，引入截图功能，在断言之前调用截图
run_test_all，设置运行哪些脚本，生成测试报告，也可以用邮件发送测试报告，此功能暂时没去实现


### 项目总结
目前只有loginPage 页面，里面也只有三个用例，一个正常登入，一个用户名类型错误，一个密码错误，其他用例需要自己补全，另一个报告只有HTML格式，报告里面没有截图，没有写注册账户页面和连接数据库操作，因为是随便选取了一个正在运营的网站，注册有手机验证码，也不知道对方的数据库密钥
