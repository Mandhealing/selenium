from selenium import webdriver
import os

def insert_img(driver,file_name):
    #定位上一级ospath
    base_dir = os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
    #转成字符串，进行替换
    base_dir = str(base_dir)
    #print(base_dir)
    base_dir = base_dir.replace('\\','/')
    # print(base_dir)
    #去掉最后一层目录
    base = base_dir.split('/test_case')[0]
    #print(base)
    #拼成截屏路径，包含图片名字
    file_path = base + '/report/image/' + file_name
    print(file_path)
    driver.get_screenshot_as_file(file_path)
    #测试一下
if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    insert_img(driver,'baidu.png')
    driver.quit()