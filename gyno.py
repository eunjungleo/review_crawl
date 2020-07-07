from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

# get path to items
get_path = 'div > div.cell_text._cell_text > div.area_text'

# open page
driver.get('https://smartstore.naver.com/liwoostore/products/3394361389#revw')


WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button_more_text")))
"""
# 더보기 버튼 펼치기
load_btns = driver.find_elements_by_class_name('button_more_text')
for i in range(1,20):
    load_btns[i].execute_script("arguments[0].click();", element)
   """ 

# get review item
# get_rvws = driver.find_elements_by_class_name('area_text')

get_user_info = driver.find_elements_by_css_selector(get_path+'div:nth-child(2) > div > span:nth-child(1)')
for user_info in get_user_info:
    print(user_info.text)

"""
# get data
pages = driver..execute_script('setAttribute(find_elements_by_class_name('page.number'),"area-selected","true");)')

# comment_id = 
user_id = driver.find_elements_by_css_selector('div.cell_text._cell_text > div.area_text > div:nth-child(2) > div > span:nth-child(1)')
for i in user_id:
    print(i.text)

comment_date = 
product_option
comment_body
product_rate
comment_likes
"""
driver.quit()