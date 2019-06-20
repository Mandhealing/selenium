#识别图片上的验证码，识别率比较低，建议大家把项目组的验证码暂时关闭
from PIL import Image, ImageGrab #pip install Pillow==5.3.0
import pytesseract #pip install pytesseract
import requests,re,os
from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
# from models.getScreen import insert_img
from time import sleep
# from getScreen import insert_img

def save_image_result(driver):
    # type ={'type':'login'}
    image_loc = ('css selector','div#captcha>img#codeimg')
    # url = 'https://passport.douguo.com'
    get_src = driver.find_element(*image_loc)

    size = get_src.size
    print(size)
    #微信截图可以定位 x y
    geti = ImageGrab.grab((1250, 600, 1350, 631))

    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]
    
    path = base + '/report/image/'+'image.png'
    re = pytesseract.image_to_string(geti)
    print(re)
    # geti.save(path)
    # f = Image.open(path)
    
    # getimage = f.crop(ra)
    geti.save(path)
    # verify = Image.open(path)
    # result = pytesseract.image_to_string(verify)
    
    result = re.replace(' ','').replace('\n','').replace('\u3000','')
    print(result)
    
    return result

    # .get_attribute('src')
    # image_url = url + get_src
    # r =requests.get('https://passport.douguo.com/captcha?type=login&t=1560692427367')
    # reg = '/captcha?type=login*'
    # getimage =re.findall(re.compile(reg))

    # with open ('verifyCode.png','wb') as f:
    #     f.write(r.content)
   
   

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://passport.douguo.com/')
    
    username_loc = ('id', "username")
    password_loc = ('id', "password")
    submit_loc = ('id', "login")
    code_loc = ('id','code')
    err_loc =('id', 'err')
    driver.find_element(*username_loc).send_keys('username') 
    driver.find_element(*password_loc).send_keys('password')
    driver.find_element(*submit_loc).click()
    sleep(3)
    result = save_image_result(driver)
    driver.find_element(*code_loc).send_keys(result)
    driver.find_element(*submit_loc).click()
    # sleep(3)
    # while driver.find_element(*err_loc).text =='验证码输入错误':
    #     result1 = save_image_result(driver)
    #     driver.find_element(*code_loc).clear()
    #     driver.find_element(*code_loc).send_keys(result1)
    #     driver.find_element(*submit_loc).click()
    #     sleep(3)
    # else:
    #     assert(driver.find_element(*err_loc).text == '登录密码错误')
