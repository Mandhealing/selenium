from selenium import webdriver

#这里并没有用远程浏览器驱动
#远程驱动的好处就是你控制远程主机的浏览器驱动帮你跑自动化用例，自己主机可以做别的事情
def browser():
    driver = webdriver.Chrome()
    return driver
#测试
if __name__ == "__main__":
    dr = browser()
    dr.get("https://www.douguo.com/")
    dr.quit()