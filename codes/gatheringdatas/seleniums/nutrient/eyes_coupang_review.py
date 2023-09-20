#!/usr/bin/env python
# coding: utf-8

# In[32]:


from selenium import webdriver
import time
import pandas as pd
import pymongo as mg
from selenium.webdriver.chrome.options import Options
import subprocess
import shutil


# In[ ]:


# 자신 맞는 chrome.exe 위치 변경 필요
subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")


# In[33]:


#open chrome browser
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1560,840")
browser = webdriver.Chrome(executable_path='../../../../chromedriver.exe', options=options) #webdriver_selenium과 web을 연결해주기위함. 


# In[34]:


# url in address window
browser.get('https://www.coupang.com/np/search?component=&q=%EB%88%88+%EC%98%81%EC%96%91%EC%A0%9C&channel=user')
browser.implicitly_wait(10)


# In[35]:


# ## 마우스 커서 올려서 하위 메뉴를 보기
# from selenium.webdriver.common.action_chains import ActionChains


# In[36]:


# # 마우스 커서를 올릴 웹 요소 선택
# element_to_hover_over = browser.find_element_by_css_selector('#searchSortingList > ul')


# In[37]:


# # ActionChains 객체 생성
# action = ActionChains(browser)
# # 마우스를 웹 요소 위에 올리기 (호버)
# action.move_to_element(element_to_hover_over).perform()


# In[38]:


# # 하위 목록의 웹 요소 선택: 72개씩 보기 
# sub_element = browser.find_element_by_css_selector('#searchSortingList > ul > li:nth-child(4) > label')
# # 하위 목록 클릭
# sub_element.click()


# In[41]:


## 제품 선택하기 
click_path='#\31 175646750 > a > dl > dd'
browser.find_element_by_css_selector(click_path).click()


# #### 제품 
