#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time
import pandas as pd
# import pymongo as mg
from selenium.webdriver.support.ui import WebDriverWait


# In[2]:


from selenium.webdriver.chrome.options import Options
import subprocess
import shutil

# 자신 맞는 chrome.exe 위치 변경 필요
subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
  # Experimental option as an argument


# In[3]:


#open chrome browser
browser = webdriver.Chrome(executable_path='../../../../../chromedriver.exe', options=options) #webdriver_selenium과 web을 연결해주기위함.
browser.set_window_size(1560,2000)


# In[4]:


# url in address window _ 눈 개선 영양제
browser.get('https://search.11st.co.kr/pc/total-search?kwd=%25EB%2588%2588%25EA%25B0%259C%25EC%2584%25A0%2520%25EC%2598%2581%25EC%2596%2591%25EC%25A0%259C&tabId=TOTAL_SEARCH')
browser.implicitly_wait(3)


# In[5]:


## 리뷰 많은 순 클릭
click_path='#layBodyWrap > div > div > div.l_search_content > div.search_content > div.c_search_sorting > div > div > div > div'
browser.find_element_by_css_selector(click_path).click()
select_category='div.c_search_sorting > div > div > div > ul > li:nth-child(5)'
browser.find_element_by_css_selector(select_category).click()


# In[6]:


## 제품 클릭하기
product_page = '#section_commonPrd > div.c-search-list > ul > li:nth-child(60)'
product_info=browser.find_element_by_css_selector(product_page)
product_info.click()


# In[7]:


## 제품 이름을가져오고싶음. 


# ### 제품정보
# - 제품명: div.c_product_info_title > h1
# 
# ### 리뷰보기 single 
# 
# - 리뷰 보기 클릭: #tabMenuDetail2
# - 리뷰 날짜: #review-list-page-area > ul:nth-child(1) > li:nth-child(4) > div.c_product_review_cont > p.side > span
# - 스크롤 내려서 리뷰 더보기를 눌러야함. 
# - 리뷰 더보기를 계속 눌러야함_리뷰가 다 나올때까지 클릭하는걸로 하자. 
#     - 이 내용은 chat에 물어보기
# - 리뷰 내용: #review-list-page-area > ul:nth-child(1) > li:nth-child(4) > div > div > div.cont_text_wrap > p
#     - 리뷰 내용이 너무 길면 : 더보기 눌러야함: div.cont_text_wrap > p.cont_btn.review-expand 이게 또 사용이 될까??
# - 리뷰 별점:#review-list-page-area > ul:nth-child(1) > li:nth-child(4) > div > p.grade > span > em
#     - .get_attribute('aria-label')
# - 리뷰 작성자: #review-list-page-area > ul:nth-child(1) > li:nth-child(4) > dl > dt
# 
# 

# In[8]:


# 새로 열린 창으로 전환
new_window_handle = None
while not new_window_handle:
    for handle in browser.window_handles:
        if handle != browser.current_window_handle:
            new_window_handle = handle
            break


# In[9]:


browser.switch_to.window(new_window_handle)


# In[10]:


# 새 창의 주소를 변수로 저장
new_window_url = browser.current_url


# In[11]:


# ## 리뷰 보기
# review_page = '#prdReview > strong'
# review_click=browser.find_element_by_css_selector(review_page)
# review_click.click()


# In[12]:


product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
product_name


# In[13]:


# 리뷰보기 클릭 불필요
browser.switch_to.frame('ifrmReview')


# In[14]:


# # 리뷰 더보기 클릭_리뷰 더보기 버튼없을때까지 누르기
# while True : 
#     try : 
#         button = '#review-list-page-area > div > button'
#         button_click=browser.find_element_by_css_selector(button)
#         button_click.click()
#         time.sleep(2) 
        
#     except:
#         print('리뷰 더보기 없음')
#         break


# In[15]:


# ## 리뷰 내용 더보기 
# text_more = 'cont_btn review-expand'
# text_click = browser.find_element_by_css_select(text_more)
# text_click.click()
# time.sleep(2)


# In[16]:


while True:
    try:
        # 리뷰 더보기 버튼을 찾습니다.
        button = '#review-list-page-area > div > button'
        button_click=browser.find_element_by_css_selector(button)
        
        # 리뷰 더보기 버튼을 클릭합니다.
        button_click.click()
        
        # 클릭 후 잠시 대기합니다 (사이트 로딩에 따라 조절)
        time.sleep(2)
        
# #         try:
# #             # 리뷰 내용 더보기 버튼을 찾습니다.
# #             content_more_selector = '.c_product_btn c_product_btn_more6 review-expand-open-text'
# #             content_more_button = browser.find_element_by_css_selector(content_more_selector)
            
# #             # 리뷰 내용 더보기 버튼을 클릭합니다.
# #             content_more_button.click()
            
# #             # 클릭 후 잠시 대기합니다 (사이트 로딩에 따라 조절)
# #             time.sleep(2)
            
#         except :
#             print('안펼쳐짐')
#             break
        
    except:
        # 리뷰 더보기 버튼을 더 이상 찾을 수 없으면 반복 종료합니다.
        print('리뷰 더보기 버튼을 더 이상 찾을 수 없음')
        break


# In[17]:


##리뷰 번들
reviews_bundle = browser.find_elements_by_css_selector('.review_list_element')
len(reviews_bundle)


# In[18]:


print(reviews_bundle[367].text)


# - collection에 넣을 column명
# ['product_name'] ['review_date'] ['review_content'] ['review_star'] [review_writer] 

# #### #review-list-page-area > ul:nth-child(2) > li:nth-child(8)
# - 리뷰 더보기를 클릭하면 ul:nth-child(2) 이게 늘어나고 그 안에서 li:nth-child(8)이게 1부터 10까지 있음. 
# 이걸 for문 돌려..

# In[19]:


# product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
review_content = reviews_bundle[17].find_element_by_css_selector('div.c_product_review_cont > div > div.cont_text_wrap > p').text ##bundle에서 0번째 가져옴?
review_date = reviews_bundle[17].find_element_by_css_selector('div.c_product_review_cont > p.side > span').text 
review_star = reviews_bundle[17].find_element_by_css_selector('p.grade > span > em').text
review_writer = reviews_bundle[17].find_element_by_css_selector('dl > dt').text 
review_content, review_date, review_star, review_writer


# ### 리뷰보기 multiple
# - 리뷰 묶음: #review-list-page-area
# 
# - 리뷰 날짜: div > p.side > span
# - 리뷰 내용: div.cont_text_wrap > p
# - 리뷰 별점: .c_seller_grade em
# - 리뷰 작성자: .c_product_reviewer dt.name

# In[20]:


## 에러 처리 필요 ::: 케어네이션... 앱은 리뷰 1.09천개로 표시됩
## 일단 총 리뷰수를 int로 바꾼다. 
review_total_count_text = browser.find_element_by_css_selector('h4 > span > i').text
    
## 혜인설명: 총 댓글 수를 정규화로 뽑아냄 .
import re # reqexpress function
result_list = re.findall(r'\d+', review_total_count_text)
# print(result_list[0], int(result_list[0]))
        
review_total_count = int(result_list[0])  # 리뷰 총 갯수
review_total_count


# In[21]:


review_standard_count_per = 10

loop_count_int = int(review_total_count / review_standard_count_per)
for count in range(1, loop_count_int+1) :
    try :
        reviews_bundle = browser.find_elements_by_css_selector('.review_list_element')
        # print('current reviews_bundle count : {}'.format(len(reviews_bundle)))
        reviews_bundle[len(reviews_bundle)-1].click()
        time.sleep(3)
    except :
        # print('pass')
        pass
print('Done', len(reviews_bundle))
print(int(loop_count_int))


# In[22]:


len(reviews_bundle)
reviews_list = list()

# 페이지 넘기기를 위한 루프 설정
for page in range(1, loop_count_int + 2):  # 1부터 loop_count_int + 1까지 반복
    # ul:nth-child(n) 설정
    ul_selector = f'ul:nth-child({page})'

    # 한 페이지당 가져올 리뷰 수 설정
    review_standard_count_per = 10

    for review_num in range(1, review_standard_count_per + 1):
        try:
            # 리뷰 내용을 가져오는 코드
            review_content = browser.find_element_by_css_selector(
                f'{ul_selector} > li:nth-child({review_num}) > div > div').text

            # "더보기" 버튼이 있는지 확인
            try:
                more_button = browser.find_element_by_css_selector(
                    f'{ul_selector} > li:nth-child({review_num}) > div > div > div > button')
                more_button.click()  # "더보기" 버튼 클릭
                review_content += more_button.find_element_by_xpath("./following-sibling::span").text
                print('펼쳐짐')
            except :
                pass

            review_date = browser.find_element_by_css_selector(
                f'{ul_selector} > li:nth-child({review_num}) > div.c_product_review_cont > p.side > span').text
            review_star = browser.find_element_by_css_selector(
                f'{ul_selector} > li:nth-child({review_num}) > div > p.grade > span > em').text
            review_writer = browser.find_element_by_css_selector(
                f'{ul_selector} > li:nth-child({review_num}) > dl > dt').text

            # 리뷰 정보를 리스트로 저장하고 리스트에 추가
            review_data = [product_name, review_content, review_date, review_star, review_writer]
            reviews_list.append(review_data)

        except Exception as e:
            print(f"Error collecting review {review_num} on page {page}: {str(e)}")

        # Check if the length of reviews_list matches reviews_bundle
        if len(reviews_list) == len(reviews_bundle):
            break  # Break out of the loop if the lengths match

    # Check again after the inner loop to break from the outer loop
    if len(reviews_list) == len(reviews_bundle):
        break

# # 웹 브라우저 종료
# browser.quit()

# 수집된 리뷰 출력 또는 저장
for review_list in reviews_list:
    print(review_list)


# In[23]:


len(reviews_list)


# In[24]:


# review_content = browser.find_element_by_css_selector('ul:nth-child(2) > li:nth-child(5) > div > div').text
# review_date = browser.find_element_by_css_selector('ul:nth-child(2) > li:nth-child(5) > div.c_product_review_cont > p.side > span').text
# review_star = browser.find_element_by_css_selector('ul:nth-child(2) > li:nth-child(5) > div > p.grade > span > em').text
# review_writer = browser.find_element_by_css_selector('ul:nth-child(2) > li:nth-child(5) > dl > dt').text
# review_content, review_date, review_star, review_writer


# In[25]:


# for n in range(1, loop_count_int + 1):  # 1부터 시작하여 n을 증가시킵니다.
#     for m in range(1, 11):  # 1부터 10까지 m을 증가시킵니다.
#         try:
#             product_name = browser.find_element_by_css_selector('div.c_product_info_title > h1').text
#             review_content = browser.find_element_by_css_selector(
#                 f'ul:nth-child({n}) > li:nth-child({m}) > div.c_product_review_cont > div > div.cont_text_wrap > p').text
#             review_date = browser.find_element_by_css_selector(
#                 f'ul:nth-child({n}) > li:nth-child({m}) > div.c_product_review_cont > p.side > span').text
#             review_star = browser.find_element_by_css_selector(
#                 f'ul:nth-child({n}) > li:nth-child({m}) > p.grade > span > em').text
#             review_writer = browser.find_element_by_css_selector(
#                 f'ul:nth-child({n}) > li:nth-child({m}) > dl > dt').text

#             # 필요한 작업 수행
#             print(product_name, review_content, review_date, review_star, review_writer)
#         except :
#             print('에러')
#             pass


# In[26]:


# reviews_list = list()
# for review_item in reviews_bundle:
#     try:
#         review_content = review_item.find_element_by_css_selector('div.c_product_review_cont > div > div.cont_text_wrap > p').text
#         review_date = review_item.find_element_by_css_selector('div.c_product_review_cont > p.side > span').text
#         review_star = review_item.find_element_by_css_selector('p.grade > span > em').text
#         review_writer = review_item.find_element_by_css_selector('dl > dt').text
#         review_list = [review_content, review_date, review_star, review_writer]
#         reviews_list.append(review_list)
#     except:
#         # 해당 리뷰 버블에서 필요한 요소를 찾을 수 없는 경우
#         # 이 부분을 처리하거나, 아무것도 하지 않도록 설정할 수 있습니다.
#         print('에러임')
#         pass


# In[ ]:




