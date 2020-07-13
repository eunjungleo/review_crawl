
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions  
import csv, time
import pandas as pd


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('lang=ko_KR')
driver = webdriver.Chrome(chromedriver, options=options) 

driver.get('https://smartstore.naver.com/liwoostore/products/3394361389#revw')

# global
get_items = []
get_user_ids = []
get_dates = []
get_options = []
get_contents = []
get_prod_ratings = []
get_comment_scores = []


# open page
while True:

    try:
        # page turner: 1-10
        for index in range(0,10):

            try:
                go_page = driver.find_elements(By.CSS_SELECTOR, ".module_pagination._review_list_page > a.page.number")
                driver.execute_script("arguments[0].click();", go_page[index])
                
            except exceptions.StaleElementReferenceException:
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".module_pagination._review_list_page > a.page")))
                go_page.clear()
                go_page = driver.find_elements_by_css_selector(".module_pagination._review_list_page > a.page.number")
                driver.execute_script("arguments[0].click();", go_page[index])

                time.sleep(5)

                # 더보기 버튼 클릭
                get_items.extend(driver.find_elements(By.CSS_SELECTOR, '.item_review._review_list_item_wrap'))
                for item in get_items:
                    driver.execute_script("arguments[0].setAttribute('class','is_opened')", item)
                    
                # 사용자 id
                get_user_ids.extend(driver.find_elements(By.CSS_SELECTOR, ".area_status_user > span:nth-child(1)"))

                # 댓글 날짜
                get_dates.extend(driver.find_elements(By.CSS_SELECTOR, ".area_status_user > span:nth-child(2)"))

                # 선택 제품
                get_options.extend(driver.find_elements(By.CSS_SELECTOR, ".area_status_user > p.text_info.text_option"))

                # 리뷰 본문
                get_contents.extend(driver.find_elements(By.CSS_SELECTOR, ".review_text._review_text"))

                # 상품 별점
                get_prod_ratings.extend(driver.find_elements(By.CSS_SELECTOR, ".number_grade"))

                # 리뷰 좋아요 수
                get_comment_scores.extend(driver.find_elements(By.CSS_SELECTOR, "span.count._count"))


        #다음 >
        try:
            go_next = driver.find_element_by_css_selector(".module_pagination._review_list_page > a.page.next")
            driver.execute_script("arguments[0].click();", go_next)
        except exceptions.StaleElementReferenceException:
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".module_pagination._review_list_page > a.page.next")))
            go_next = driver.find_element_by_css_selector(".module_pagination._review_list_page > a.page.next")
            driver.execute_script("arguments[0].click();", go_next)

        # csv
        f = open('ebs.csv', mode='a', encoding='utf-8', newline='')
        wr = csv.writer(f)

        for list in zip(go_page, get_items, get_user_ids, get_dates, get_options, get_prod_ratings, get_comment_scores, get_contents):
            page_num = list[0].text
            comment_pk = list[1].get_attribute("id").text.replace("_","")
            user_id = list[2].text
            date = list[3].text
            prod_choice = list[4].text
            prod_rating = list[5].text
            comment_likes = list[6].text
            comment_body = list[7].text
            wr.writerow([page_num, comment_pk, user_id, date, prod_choice, prod_rating, comment_likes, comment_body])

    except:
        break
            
driver.quit()

# 중복 제거
file_name = "review.csv"
file_name_output = "review_done.csv"
df = pd.read_csv(file_name, sep="\t or ,")
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(file_name_output)