from HTMLTestRunner import HTMLTestRunner #这个文件需要放在python的lib目录里面
import unittest, time, os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# ===========查找测试报告目录，找到最新生成的测试报告文件================
def new_report(testreprot):
    lists = os.listdir(testreprot)
    print(lists)
    lists.sort(key = lambda fn: os.path.getatime (testreprot+ "\\" + fn))
    file_new = os.path.join(testreprot,lists[-1])
    print(file_new)
    return file_new

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    print(now)
    filename = './WebAuto/report/' + now + 'result.html'
    print(filename)
    with open(filename, 'wb') as f:
        runner = HTMLTestRunner(stream = f, 
        title ='自动化测试报告', 
        description = "环境：Win10 浏览器：chrome")
        discover = unittest.defaultTestLoader.discover('./WebAuto/test_case',pattern='*test.py')
        print(discover)
        runner.run(discover)