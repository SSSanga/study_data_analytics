
from selenium import webdriver
import time
import pandas as pd





import pymongo as mg
client = mg.MongoClient(host='mongodb://localhost:27017')
database = client['study_test']
collection = database['eyes_review']




from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.options import Options
import subprocess
import shutil


# In[ ]:


# 자신 맞는 chrome.exe 위치 변경 필요
subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
  # Experimental option as an argument


# In[ ]:


#open chrome browser
browser = webdriver.Chrome(executable_path='C:/Users/01-15/Develops/chromedriver.exe', options=options) #webdriver_selenium과 web을 연결해주기위함.
browser.set_window_size(1560,2000)


# In[ ]:


# url in address window
browser.get('https://search.11st.co.kr/pc/total-search?kwd=%25EB%2588%2588%25EA%25B0%259C%25EC%2584%25A0%2520%25EC%2598%2581%25EC%2596%2591%25EC%25A0%259C&tabId=TOTAL_SEARCH')
browser.implicitly_wait(10)


# In[ ]:


## 리뷰 많은 순 클릭
click_path='#layBodyWrap > div > div > div.l_search_content > div.search_content > div.c_search_sorting > div > div > div > div'
browser.find_element_by_css_selector(click_path).click()
select_category='div.c_search_sorting > div > div > div > ul > li:nth-child(5)'
browser.find_element_by_css_selector(select_category).click()


# In[ ]:


## pagination 하기
# 검색 결과 # div.search_content > div > p > span
product_total = browser.find_element_by_css_selector('div.search_content > div > p > span')
product_total_str = product_total.text
# 쉼표를 제거합니다.
product_total_del = product_total_str.replace(',', '')
product_total_count = int(product_total_del)


# In[ ]:


print(product_total_count) ## 검색 결과_숫자

product_standard_count_per = 60 ## 상품목록수


# In[ ]:


loop_count_int = int(product_total_count / product_standard_count_per) 
print(loop_count_int) ## 상품 총 페이지수 


# # In[ ]:
second_page = '#section_commonPrd > nav > ul > li:nth-child(3) > button'
second_click = browser.find_element_by_css_selector(second_page)
second_click.click()
# 현재 페이지 번호를 초기화합니다.
current_page = 2

# pagination 버튼을 끝까지 순환하면서 페이지 이동합니다.
while current_page <= loop_count_int:
    for i in range(2, 4):  # 1부터 60까지 순회합니다.
        try:
            product_page = f'#section_commonPrd > div.c-search-list > ul > li:nth-child({i}) > div > a'
            product = browser.find_element_by_css_selector(product_page)
            product.click()
            # 새로 열린 창으로 브라우저 컨텍스트를 전환합니다.
            browser.switch_to.window(browser.window_handles[-1]) 
            browser.implicitly_wait(2)
            ## -> browser.window_handles[-]하면 옆으로 쭉쭉 생기는건가봄. 
            ## 여기부터 리뷰 더보기 클릭하기 
            product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
            print(product_name)
            # 리뷰보기 클릭 불필요
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
            review_total_count
            if review_total_count == 0:
                print('리뷰가 없어 종료합니다.')
                break
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
            len(reviews_bundle)

            ## 리뷰 리스트
            eyes_product_columns_name = ['product_name','review_content', 'review_date', 'review_star', 'review_writer']
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
            # df_reviews = pd.DataFame(data=reviews_list, columns=eyes_product_columns_name)
            # data_dict = df_reviews.to_dict(orient='records')
            # collection.insert_many(data_dict)
            print(len(reviews_list))

            # 현재 페이지를 닫습니다.
            browser.close()
            # 다음 상품을 클릭하기 전에 원래의 창으로 다시 전환합니다.
            browser.switch_to.window(browser.window_handles[0])
                        
        except:
            print(f'에러: {i}')
            pass
        # Pagination 버튼을 클릭합니다.
    current_page += 1
    page_button_css = f'#section_commonPrd > nav > ul > li:nth-child({current_page % 10 + 2}) > button'
    page_button = browser.find_element_by_css_selector(page_button_css)
    page_button.click()
    
    # 10번째 페이지일 경우 next 버튼 클릭
    # if current_page % 10 == 0:
    #     next_button = browser.find_element_by_css_selector('#section_commonPrd > nav > ul > li.next > button')
    #     next_button.click()
    ## current_page가 4면 stop
    if current_page % 4 == 0:
        break



# product_name= browser.find_element_by_css_selector('div.c_product_info_title > h1').text
# product_name
# # 리뷰보기 클릭 불필요
# browser.switch_to.frame('ifrmReview')
# while True:
#     try:
#         # 리뷰 더보기 버튼을 찾습니다.
#         button = '#review-list-page-area > div > button'
#         button_click=browser.find_element_by_css_selector(button)
        
#         # 리뷰 더보기 버튼을 클릭합니다.
#         button_click.click()
        
#         # 클릭 후 잠시 대기합니다 (사이트 로딩에 따라 조절)
#         time.sleep(2)
#     except:
#         # 리뷰 더보기 버튼을 더 이상 찾을 수 없으면 반복 종료합니다.
#         print('리뷰 더보기 버튼을 더 이상 찾을 수 없음')
#         break



##리뷰 번들
reviews_bundle = browser.find_elements_by_css_selector('.review_list_element')
len(reviews_bundle)


# In[ ]:


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


# In[ ]:


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


# In[ ]:


len(reviews_list)

