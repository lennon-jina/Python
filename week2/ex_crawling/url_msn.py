# pip install selenium
# pip install chromedriver_autoinstaller
from selenium import webdriver
import chromedriver_autoinstaller
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 최초의 한번은
chromedriver_autoinstaller.install()  # 한 번 설치하면 다음부터는 호출 안 해도 됨.
driver = webdriver.Chrome()  # C <-- 대문자
driver.implicitly_wait(3)    # 브라우저가 켜질 때까지 기다리기
url = "https://www.msn.com/ko-kr/channel/topic/%ED%99%94%EC%A0%9C%EC%9D%98%EB%89%B4%EC%8A%A4/tp-Y_08e2dfa5-fc63-4143-a127-2c4963904232?ocid=hpmsn&cvid=b6f8ee95a566496ea4999aac50753f56"
driver.get(url)  # msn 사이트가 느림.
time.sleep(1)    # 1초 기다리기
pagedown = 1
body = driver.find_element(By.TAG_NAME, 'body')  # 스크롤 대상
while pagedown < 10:
    body.send_keys(Keys.PAGE_DOWN)  # 스크롤 내리기
    time.sleep(1)
    pagedown += 1
driver.quit()    # 종료(브라우저 닫기)