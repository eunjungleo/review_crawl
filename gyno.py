from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions  
import csv, time


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

driver.get('https://smartstore.naver.com/liwoostore/products/3394361389#revw')

# open page
while True:
    for index in range(0,9):
        try:
            go_page = driver.find_elements_by_css_selector(".module_pagination._review_list_page > a.page")
            driver.execute_script("arguments[0].click();", go_page[index])

        except exceptions.StaleElementReferenceException:
            print('e')

            time.sleep(5)

            # load more
            get_items = driver.find_elements_by_css_selector('.item_review._review_list_item_wrap')
            for item in get_items:
                print(item.get_attribute('id'))

    go_next = driver.find_element_by_css_selector(".module_pagination._review_list_page > a.page.next")
    driver.execute_script("arguments[0].click();", go_next)

"""
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