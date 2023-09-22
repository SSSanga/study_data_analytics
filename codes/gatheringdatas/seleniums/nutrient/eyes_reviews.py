from selenium import webdriver
import time
import pandas as pd


# In[2]:


import pymongo as mg
client = mg.MongoClient(host='mongodb://localhost:27017')
database = client['study_test']
collection = database['anything_review']


# In[3]:


from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
import subprocess
import shutil


# In[4]:


subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


# In[5]:


#open chrome browser
browser = webdriver.Chrome(executable_path='C:/Users/01-15/Develops/chromedriver.exe', options=options) #webdriver_selenium과 web을 연결해주기위함.
browser.set_window_size(1560,2000)


# In[6]:


# url in address window
browser.get('https://search.11st.co.kr/pc/total-search?kwd=%25EB%2588%2588%25ED%2594%25BC%25EB%25A1%259C%25EA%25B0%259C%25EC%2584%25A0%2520%25EC%2598%2581%25EC%2596%2591%25EC%25A0%259C&tabId=TOTAL_SEARCH&sortCd=I&pageNo=1')
browser.implicitly_wait(5)

product_page = '#section_commonPrd > div.c-search-list > ul > li:nth-child(3) > div > a'
product = browser.find_element_by_css_selector(product_page)
product.click()
browser.switch_to.window(browser.window_handles[-1]) 

## 여기부터 리뷰 더보기 클릭하기 
product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
print(product_name)
browser.switch_to.frame('ifrmReview')
while True:
    try:
        # 리뷰 더보기 버튼을 찾습니다.
        button = '#review-list-page-area > div > button'
        button_click=browser.find_element_by_css_selector(button)
                    
        # 리뷰 더보기 버튼을 클릭합니다.
        button_click.click()
                    
        # 클릭 후 잠시 대기합니다 (사이트 로딩에 따라 조절)
        time.sleep(2)
    except:
        # 리뷰 더보기 버튼을 더 이상 찾을 수 없으면 반복 종료합니다.
        print('리뷰 더보기 버튼을 더 이상 찾을 수 없음')
        break

##리뷰 번들
reviews_bundle = browser.find_elements_by_css_selector('.review_list_element')
len(reviews_bundle)
## 일단 총 리뷰수를 int로 바꾼다. 
review_total_count_text = browser.find_element_by_css_selector('h4 > span > i').text
                
## 혜인설명: 총 댓글 수를 정규화로 뽑아냄 .
import re # reqexpress function
result_list = re.findall(r'\d+', review_total_count_text)
# print(result_list[0], int(result_list[0]))
                    
review_total_count = int(result_list[0])  # 리뷰 총 갯수
print(review_total_count)
if review_total_count < 10:
    # 단일 리뷰 펼치기
    
    review_bundle = browser.find_elements_by_css_selector('.review_list_element')
    len(review_bundle)

    ul_index = 1
    li_index = 1

    for i in range(1, len(review_bundle)+1):
        try:
            time.sleep(1)
            expand_button_css_selector = f'#review-list-page-area > ul:nth-child({ul_index}) > li:nth-child({li_index}) > div > div > div.cont_text_wrap > p.cont_btn.review-expand > button.c_product_btn.c_product_btn_more6.review-expand-open-text' 
            expand_button = browser.find_elements_by_css_selector(expand_button_css_selector)

            expand_button[0].click()  # Click the button if it exists 
        except:
            pass
        if li_index == 10:
            ul_index += 1
            li_index = 1
        else:
            li_index += 1
                        
    review_standard_count_per = 10
    loop_count_int = int(review_total_count / review_standard_count_per)
    print('Done', len(reviews_bundle), loop_count_int)




    ## 리뷰 리스트
    eyes_product_columns_name = ['product_name','review_content', 'review_date', 'review_star', 'review_writer']
    reviews_list = list()

    for page in range(1, loop_count_int + 2):  # 1부터 loop_count_int + 1까지 반복
        # ul:nth-child(n) 설정
        ul_selector = f'ul:nth-child({page})'

        # 한 페이지당 가져올 리뷰 수 설정
        review_standard_count_per = 10

        for review_num in range(1, review_standard_count_per + 1):
            try:
                # 리뷰 내용을 가져오는 코드
                review_content = browser.find_element_by_css_selector(f'{ul_selector} > li:nth-child({review_num}) > div > div').text
                review_date = browser.find_element_by_css_selector(f'{ul_selector} > li:nth-child({review_num}) > div.c_product_review_cont > p.side > span').text
                review_star = browser.find_element_by_css_selector(f'{ul_selector} > li:nth-child({review_num}) > div > p.grade > span > em').text
                review_writer = browser.find_element_by_css_selector(f'{ul_selector} > li:nth-child({review_num}) > dl > dt').text

                # 리뷰 정보를 리스트로 저장하고 리스트에 추가
                review_data = [product_name, review_content, review_date, review_star, review_writer]
                reviews_list.append(review_data)
                print(reviews_list)
            except Exception as e:
                print(f"Error collecting review {review_num} on page {page}: {str(e)}")
    
else:        
    print('리뷰 총 개수가 0이므로 종료합니다.')
