from selenium import webdriver
import login_info
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/illo.yoon/Workspace/Python/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://www.pinterest.com/')


button_login_window = driver.find_element_by_css_selector('#__PWS_ROOT__ > div:nth-child(1) > div > div > div > div:nth-child(2) > div.Jea._he.b8T.gjz.zI7.iyn.Hsu > div.Jea.l7T.zI7.iyn.Hsu > div:nth-child(2) > button')
button_login_window.click()

input_email = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[1]/fieldset/span/div/input')
input_password = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[2]/fieldset/span/div/input')

input_email.send_keys(login_info.login_info['id'])
input_password.send_keys(login_info.login_info['pw'])

button_login = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[5]/button')
button_login.click()

time.sleep(20)
driver.implicitly_wait(10)

input_search_keyword = driver.find_element_by_css_selector('#searchBoxContainer > div > div > div.ujU.zI7.iyn.Hsu > input[type=text]')
input_search_keyword.send_keys('hand without ring')
input_search_keyword.send_keys(Keys.ENTER)

driver.implicitly_wait(5)


print('hello')