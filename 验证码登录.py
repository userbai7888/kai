from selenium import webdriver
from PIL import Image
import pytesseract
import os,time
#chromedriver = "D:\Program Files\Anaconda3\selenium\webdriver\chromedriver.exe" #这里写本地的chromedriver 的所在路径
#os.environ["webdriver.Chrome.driver"] = chromedriver #调用chrome浏览器
driver = webdriver.Chrome()
driver.get("http://xxxx.com") #该处为具体网址
driver.refresh() #刷新页面
driver.maximize_window() #浏览器最大化
#获取全屏图片，并截取验证码图片的位置
driver.get_screenshot_as_file('a.png')
location = driver.find_element_by_id('imgValidateCode').location
size = driver.find_element_by_id('imgValidateCode').size
left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']
a = Image.open("a.png")
im = a.crop((left,top,right,bottom))
im.save('a.png')
time.sleep(1)
#打开保存的验证码图片
image = Image.open("a.png")
#图片转换成字符
vcode = pytesseract.image_to_string(image)
print(vcode)
#填充用户名 密码 验证码
driver.find_element_by_id("staffCode").send_keys("username")
driver.find_element_by_id("pwd").send_keys("password")
driver.find_element_by_id("validateCode").send_keys(vcode)
#点击登录
driver.find_element_by_id("loginBtn").click()