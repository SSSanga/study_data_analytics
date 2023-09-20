from selenium import webdriver
import time

options = webdriver.ChromeOptions()
# 브라우저 창 크기 설정
options.add_argument("--window-size=1300,800")

# open chrome browser
browser = webdriver.Chrome(executable_path='../chromedriver.exe', options=options)

# url in address window(주소창에 url 입력)
browser.get('https://www.11st.co.kr/products/2944672103?&trTypeCd=PW24&trCtgrNo=585021')
browser.implicitly_wait(10)

# 리뷰보기 클릭 불필요
browser.switch_to.frame('ifrmReview')
results = browser.find_elements_by_css_selector('#review-list-page-area > ul > li')
# len(results)
# result = browser.find_element_by_css_selector('#review-list-page-area > ul > li')

# click 방식
# browser.find_element_by_xpath('//*[@id="review-list-page-area"]/div/button').click()
## 위에 방식 동작되지 않을 때
from selenium.webdriver.common.keys import Keys
browser.find_element_by_xpath('//*[@id="review-list-page-area"]/div/button').send_keys(Keys.ENTER)
pass