from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from time import sleep
import requests

url_to_scrap = 'https://jo.opensooq.com/en/cars/cars-for-sale'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url_to_scrap)

source_data = driver.page_source
soup = bs(source_data, features="html.parser")

main_counter_div = soup.find('div', {'id': 'title_wrap'})
total_page_posts_text = main_counter_div.find('span', {'class': 'inline'}).text
total_page_posts_count = int(total_page_posts_text.split(' ')[2])

element_count = 0

print(f'Total Posts count: {total_page_posts_count}')

for i in range(total_page_posts_count):
    item = driver.find_element_by_xpath(f"//ul[@id='gridPostListing']/li")[element_count]
    print(item)
    element_count = element_count + 1
# python_button = driver.find_elements_by_xpath(
#     "//i[@class='rectLi']")[element_count]
# python_button.click()
