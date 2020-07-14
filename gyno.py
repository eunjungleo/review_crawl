
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions  
import csv, time
import pandas as pd


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)


driver.get('https://smartstore.naver.com/liwoostore/products/3394361389#revw')


# open page
while True:
    time.sleep(2)
    # page turner: 1-10
    for index in range(0,11):
        if index < 10:
            try:
                go_page = driver.find_elements(By.CSS_SELECTOR, ".module_pagination._review_list_page > a.page.number")
                page_num = go_page[index].text
                print(page_num)
                driver.execute_script("arguments[0].click();", go_page[index])
            except exceptions.StaleElementReferenceException:
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".module_pagination._review_list_page > a.page.number")))
                go_page.clear()
                go_page = driver.find_elements_by_css_selector(".module_pagination._review_list_page > a.page.number")
                print(page_num)
                driver.execute_script("arguments[0].click();", go_page[index])
            except IndexError:
                time.sleep(5)
                pass
        
                    
            WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".item_review._review_list_item_wrap")))

            try:
                get_items = driver.find_elements(By.CSS_SELECTOR, '.item_review._review_list_item_wrap')
                for item in get_items:
                    get_items = driver.find_elements(By.CSS_SELECTOR, '.item_review._review_list_item_wrap')
                    driver.execute_script("arguments[0].click();", item)

            except exceptions.StaleElementReferenceException:
                time.sleep(10)
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".item_review._review_list_item_wrap")))
                get_items = driver.find_elements(By.CSS_SELECTOR, '.item_review._review_list_item_wrap')
                for item in get_items:
                    driver.execute_script("arguments[0].click();", item)

            get_user_ids = driver.find_elements(By.CSS_SELECTOR, ".area_status_user > span:nth-child(1)")
            get_dates = driver.find_elements(By.CSS_SELECTOR, ".area_status_user > span:nth-child(2)")
            get_options = driver.find_elements(By.CSS_SELECTOR, ".area_status_user > p.text_info.text_option")
            get_contents = driver.find_elements(By.CSS_SELECTOR, ".review_text._review_text")
            get_prod_ratings = driver.find_elements(By.CSS_SELECTOR, ".number_grade")
            get_comment_scores = driver.find_elements(By.CSS_SELECTOR, "span.count._count")
            get_items.clear()
            get_items = driver.find_elements(By.CSS_SELECTOR, '.item_review._review_list_item_wrap')

            user_id = []
            date = []
            prod_choice = []
            comment_body = []
            prod_rating = []
            comment_likes = []
            comment_pk = []

            for i in range(0, 21):
                try:
                    user_id.append(str(get_user_ids[i].text))
                    date.append(str(get_dates[i].text))
                    prod_choice.append(str(get_options[i].text))
                    comment_body.append(str(get_contents[i].text).replace("\n", " "))
                    prod_rating.append(int(get_prod_ratings[i].text))
                    comment_likes.append(int(get_comment_scores[i].text))
                    comment_pk.append(str(get_items[i].get_attribute('id')))
                except IndexError:
                    pass
                except exceptions.StaleElementReferenceException:
                    time.sleep(5)
                    user_id.append(str(get_user_ids[i].text))
                    date.append(str(get_dates[i].text))
                    prod_choice.append(str(get_options[i].text))
                    comment_body.append(str(get_contents[i].text).replace("\n", " "))
                    prod_rating.append(int(get_prod_ratings[i].text))
                    comment_likes.append(int(get_comment_scores[i].text))
                    comment_pk.append(str(get_items[i].get_attribute('id')))
                

            get_data = zip(comment_pk, user_id, date, prod_choice, prod_rating, comment_likes, comment_body)

            for list in get_data:
                comment_pk = list[0]
                user_id = list[1]
                date = list[2]
                prod_choice = list[3]
                prod_rating = list[4]
                comment_likes = list[5]
                comment_body = list[6]

                # csv
                f = open('review1.csv', mode='a', encoding='utf-8', newline='')
                wr = csv.writer(f)
                wr.writerow([page_num, comment_pk, user_id, date, prod_choice, prod_rating, comment_likes, comment_body])

        #다음 >
        elif index==10:
            try:
                go_next = driver.find_element(By.CSS_SELECTOR, ".module_pagination._review_list_page > a.page.next")
                driver.execute_script("arguments[0].click();", go_next)
            except exceptions.StaleElementReferenceException:
                go_next.clear()
                WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".module_pagination._review_list_page > a.page.next")))
                go_next = driver.find_element(By.CSS_SELECTOR, ".module_pagination._review_list_page:last-child")
                driver.execute_script("arguments[0].click();", go_next)
            except IndexError:
                print("done")
            continue
            break
driver.quit()
"""
# 중복 제거
file_name = "review.csv"
file_name_output = "review_done.csv"
df = pd.read_csv(file_name)
df.drop_duplicates(subset=None, inplace=True)
df.to_csv(file_name_output)
"""