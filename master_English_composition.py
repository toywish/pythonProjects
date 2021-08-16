from selenium import webdriver
from time import sleep
#需要Google浏览器与chromedriver.exe, 具体可参考下载https://blog.csdn.net/weixin_42403127/article/details/85255891
username = ""  # 用户名
password = ""  # 密码
i = 0  # 0,1,2,3 对应第i-1篇作文
article_title_name = "title_name"  # 作文标题
article_body = "article_body"  # 文章正文，正文中不可含回车，需要在网页中手动分段

driver = webdriver.Chrome()
driver.get('https://sso.unipus.cn/sso/login?service=http://iwrite.unipus.cn/system/login')  # 此处填网站
driver.maximize_window()  # 浏览器最大化

user_name = driver.find_element_by_name("username")
user_name.send_keys(username)  # 输入用户名
sleep(1)
pwd = driver.find_element_by_name("password")
pwd.send_keys(password)  # 输入密码
sleep(1)
login = driver.find_element_by_id("login")
login.click()  # 登录
sleep(1)
compositions = driver.find_elements_by_class_name("shezhi")
composition = compositions[i]
composition.click()  # 进入作文页面
sleep(1)
article_title = driver.find_element_by_id("titleValueId")
article_title.send_keys(article_title_name)  # 输入作文标题
sleep(1)
driver.switch_to.frame('ueditor_0')
driver.find_element('tag name', 'body').send_keys(article_body)  # 输入作文正文

# 最后手动保存提交