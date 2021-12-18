from selenium import webdriver
import login_info
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import requests
import os
import conf

driver = webdriver.Chrome(conf.chromedriver_path)
driver.implicitly_wait(3)

# url에 접근한다.
driver.get('https://www.pinterest.com/')
driver.implicitly_wait(3)
time.sleep(5)

# 로그인 버튼 찾아서 클릭
button_login_window = driver.find_element_by_css_selector('#__PWS_ROOT__ > div:nth-child(1) > div > div > div > div:nth-child(2) > div.Jea._he.b8T.gjz.zI7.iyn.Hsu > div.Jea.l7T.zI7.iyn.Hsu > div:nth-child(2) > button')
button_login_window.click()

# 이메일, 비밀번호 폼 찾기
input_email = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[1]/fieldset/span/div/input')
input_password = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[2]/fieldset/span/div/input')

# 이메일, 비밀번호 입력하기
input_email.send_keys(login_info.login_info['id'])
input_password.send_keys(login_info.login_info['pw'])

# 로그인 버튼 누르기
button_login = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[5]/button')
button_login.click()

# 로그인하는데 시간이 좀 걸려서 넉넉하게 기다린다
time.sleep(20)
driver.implicitly_wait(10)

# 검색어 입력하기
input_search_keyword = driver.find_element_by_css_selector('#searchBoxContainer > div > div > div.ujU.zI7.iyn.Hsu > input[type=text]')
input_search_keyword.send_keys(conf.search_word)
input_search_keyword.send_keys(Keys.ENTER)

driver.implicitly_wait(5)

imagedir = 'images'
try:
    os.makedirs(imagedir, exist_ok=True)
except :
    pass

target_num_images = conf.target_num_images
links_saved = set()

# LOOP
while True:
    try:
        # get images
        images = driver.find_elements_by_xpath("//img[@srcset]")

        for image in images:
            try:
                links = image.get_property('srcset')
                url = list(filter(lambda x: x.startswith('https'), links.split(' ')))[-1]
                if url not in links_saved:
                    links_saved.add(url)

                    # download image
                    imagename = url[url.rfind('/')+1:]
                    response = requests.get(url)
                    file = open(imagedir + '/'+imagename, "wb")
                    file.write(response.content)
                    file.close()
            except Exception as e:
                pass

        if len(links_saved) > target_num_images:
            break

        if len(images)>0:
            action = ActionChains(driver)
            action.move_to_element(images[-1]).perform()
        else:
            break
        pass
    except Exception as e:
        pass
