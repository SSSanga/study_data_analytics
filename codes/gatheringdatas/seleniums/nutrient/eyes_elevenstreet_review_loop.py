
from selenium import webdriver
import time
import pandas as pd
# import pymongo as mg
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
import subprocess
import shutil

# 자신 맞는 chrome.exe 위치 변경 필요
subprocess.Popen(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
  # Experimental option as an argument


#open chrome browser
browser = webdriver.Chrome(executable_path='C:/Users/user/Develops/chromedriver.exe', options=options) #webdriver_selenium과 web을 연결해주기위함.
browser.set_window_size(1560,2000)


# url in address window
browser.get('https://search.11st.co.kr/pc/total-search?kwd=%25EB%2588%2588%2520%25EC%2598%2581%25EC%2596%2591%25EC%25A0%259C&tabId=TOTAL_SEARCH')
browser.implicitly_wait(10)


## 리뷰 많은 순 클릭
click_path='#layBodyWrap > div > div > div.l_search_content > div.search_content > div.c_search_sorting > div > div > div > div'
browser.find_element_by_css_selector(click_path).click()
select_category='div.c_search_sorting > div > div > div > ul > li:nth-child(5)'
browser.find_element_by_css_selector(select_category).click()
pass

# 리뷰를 긁어오는 순서
# 1. 상품 페이지네이션이 돌아간다. 
    #2. 상품 클릭 loop가 돌아간다. 
        # 3. 리뷰 loop가 돌아간다. 
        # 리뷰 loop가 끝나면
    # 상품 클릭 loop가 끝난다. 
# 상품 클릭 loop가 끝나면 상품 페이지네이션이 진행된다. 
# 상품 페이지네이션이 끝난다. 


# ## 제품 클릭하기
# product_page = '#section_commonPrd > div.c-search-list > ul > li:nth-child(1)'
# product_info=browser.find_element_by_css_selector(product_page)
# product_info.click()

## 제품 looping 돌리기
# 일단 1page에 #section_commonPrd > div.c-search-list > ul > li 60개 
products_path = '#section_commonPrd > div.c-search-list > ul > li'
products_list = browser.find_elements_by_css_selector(products_path)
countperpage=int(len(products_list))
print(type(products_list))
print(products_list[5])

products_name = list()
pass
for item in range(1,countperpage + 1):
    try:
        browser.find_element_by_class_name(f'#section_commonPrd > div.c-search-list > ul > li:nth-child({item}) > div > div.c-card-item__button').click()  # 각 요소를 클릭합니다.
        
        # 새로운 창 또는 탭을 열었을 경우, 다음 라인으로 이동합니다.
        browser.switch_to.window(browser.window_handles[-1])
        
        # 클릭한 페이지에서 원하는 작업을 수행합니다.
        product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
        products_list.append(product_name)
        print(products_list)
        # 작업이 끝난 후, 현재 창을 닫습니다.
        browser.close()
        
        # 원래 창으로 다시 돌아갑니다.
        browser.switch_to.window(browser.window_handles[0])
        
    except Exception as e:
        print(f"클릭 중 오류 발생: {e}")


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


# # 새로 열린 창으로 전환
# new_window_handle = None
# while not new_window_handle:
#     for handle in browser.window_handles:
#         if handle != browser.current_window_handle:
#             new_window_handle = handle
#             break


# # In[9]:


# browser.switch_to.window(new_window_handle)


# # In[10]:


# # 새 창의 주소를 변수로 저장
# new_window_url = browser.current_url


# # In[11]:


# # ## 리뷰 보기
# # review_page = '#prdReview > strong'
# # review_click=browser.find_element_by_css_selector(review_page)
# # review_click.click()


# # In[12]:


# product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
# product_name


# # In[13]:


# # 리뷰보기 클릭 불필요
# browser.switch_to.frame('ifrmReview')


# # In[14]:


# # # 리뷰 더보기 클릭_리뷰 더보기 버튼없을때까지 누르기
# # while True : 
# #     try : 
# #         button = '#review-list-page-area > div > button'
# #         button_click=browser.find_element_by_css_selector(button)
# #         button_click.click()
# #         time.sleep(2) 
        
# #     except:
# #         print('리뷰 더보기 없음')
# #         break


# # In[15]:


# # ## 리뷰 내용 더보기 
# # text_more = 'cont_btn review-expand'
# # text_click = browser.find_element_by_css_select(text_more)
# # text_click.click()
# # time.sleep(2)


# # In[18]:


# while True:
#     try:
#         # 리뷰 더보기 버튼을 찾습니다.
#         button = '#review-list-page-area > div > button'
#         button_click=browser.find_element_by_css_selector(button)
        
#         # 리뷰 더보기 버튼을 클릭합니다.
#         button_click.click()
        
#         # 클릭 후 잠시 대기합니다 (사이트 로딩에 따라 조절)
#         time.sleep(2)
        
#         try:
#             # 리뷰 내용 더보기 버튼을 찾습니다.
#             content_more_selector = 'button.c_product_btn.c_product_btn_more6.review-expand-open-text'
#             content_more_button = browser.find_element_by_css_selector(content_more_selector)
            
#             # 리뷰 내용 더보기 버튼을 클릭합니다.
#             content_more_button.click()
            
#             # 클릭 후 잠시 대기합니다 (사이트 로딩에 따라 조절)
#             time.sleep(2)
            
#         except :
#             continue
        
#     except:
#         # 리뷰 더보기 버튼을 더 이상 찾을 수 없으면 반복 종료합니다.
#         print('리뷰 더보기 버튼을 더 이상 찾을 수 없음')
#         break


# # In[17]:


# ##리뷰 번들
# reviews_bundle = browser.find_elements_by_css_selector('#review-list-page-area > ul > li')
# len(reviews_bundle)


# # In[48]:


# print(reviews_bundle[0].text)


# # - collection에 넣을 column명
# # ['product_name'] ['review_date'] ['review_content'] ['review_star'] [review_writer] 

# # In[49]:


# # product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
# review_content = reviews_bundle[0].find_element_by_css_selector('div.c_product_review_cont > div > div.cont_text_wrap > p').text ##bundle에서 0번째 가져옴?
# review_date = reviews_bundle[0].find_element_by_css_selector('div.c_product_review_cont > p.side > span').text 
# review_star = reviews_bundle[0].find_element_by_css_selector('p.grade > span > em').text
# review_writer = reviews_bundle[0].find_element_by_css_selector('dl > dt').text 
# review_content, review_date, review_star, review_writer


# # ### 리뷰보기 multiple
# # - 리뷰 묶음: #review-list-page-area
# # 
# # - 리뷰 날짜: div > p.side > span
# # - 리뷰 내용: div.cont_text_wrap > p
# # - 리뷰 별점: .c_seller_grade em
# # - 리뷰 작성자: .c_product_reviewer dt.name

# # In[ ]:


# ### loaded된 전체 review 가져오기. 
# reviews_list = list()
# for revew_item in reviews_bundle :
#     review_content = revew_item.find_element_by_css_selector('div.c_product_review_cont > div > div.cont_text_wrap > p').text ##bundle에서 0번째 가져옴?
#     review_date = revew_item.find_element_by_css_selector('div.c_product_review_cont > p.side > span').text 
#     review_star = revew_item.find_element_by_css_selector('p.grade > span > em').text
#     review_writer = revew_item.find_element_by_css_selector('dl > dt').text 
#     review_list = [review_content, review_date, review_star, review_writer]
#     reviews_list.append(review_list)
    
# len(reviews_list)

