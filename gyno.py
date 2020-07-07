from selenium import webdriver
import csv


chromedriver = 'chromedriver.exe'
driver = webdriver.Chrome(chromedriver)

# open page
driver.get('https://smartstore.naver.com/liwoostore/products/3394361389#revw')

driver.quit()