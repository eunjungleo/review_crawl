from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv, time


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)


# open page
driver.get('https://smartstore.naver.com/liwoostore/products/3394361389#revw')

page = driver.find_elements_by_css_selector('nav._review_list_page > nav > a.page.number')
print(page)
"""
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button_more_text")))

    # load more
    load_btns = driver.find_elements_by_class_name('button_more_text')
    for i in range(0,19):
        load_btns[i].send_keys('\n')

    # user id
    get_user_id = driver.find_elements(By.CSS_SELECTOR, ".area_status_user > span:nth-child(1)")
    for u in get_user_id:
        print(u.text)

    # date
    get_date = driver.find_elements(By.CSS_SELECTOR, ".area_status_user > span:nth-child(2)")
    for u in get_date:
        print(u.text)

    # product_option
    get_option = driver.find_elements(By.CSS_SELECTOR, ".area_status_user > p.text_info.text_option")
    for u in get_option:
        print(u.text)

    # comment body
    get_body = driver.find_elements(By.CSS_SELECTOR, ".review_text._review_text")
    for u in get_body:
        print(u.text)

    # stars
    get_stars = driver.find_elements(By.CSS_SELECTOR, ".number_grade")
    for u in get_stars:
        print(u.text)

    # comment likes 
    get_comment_likes = driver.find_elements(By.CSS_SELECTOR, "span.count._count")
    for u in get_comment_likes:
        print(u.text)
"""

driver.quit()