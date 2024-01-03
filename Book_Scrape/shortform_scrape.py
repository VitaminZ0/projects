from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import openpyxl
from time import sleep
import auth_keys

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://www.shortform.com/app/login?redirect=/app/books/list/all?sort=title')

email_field = driver.find_element(By.ID, 'login_email')
email_field.send_keys(auth_keys.email)
password_field = driver.find_element(By.ID, 'login_password')
password_field.send_keys(auth_keys.password)
password_field.send_keys(Keys.ENTER)

sleep(5)
driver.get('https://www.shortform.com/app/books/list/all?sort=title')

#this page is weird, it doesn't have a scroll bar, so we have to scroll down manually
print('scrolling down')
sleep(15)
iframe = driver.find_element(By.TAG_NAME, "iframe")
driver.switch_to.frame(iframe)
driver.execute_script("arguments[0].setAttribute('scrolling', 'yes')", iframe)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
print('done scrolling down')

books = driver.find_elements(By.CLASS_NAME, 'books__item')

entire_book = []

for book in books:
    string = book.text
    new_string = string.replace('\n', '|')
    list = new_string.split('|')
    
    if 'FREE' in list[0]:
        list.pop(0)
        
    elif 'Subscribe' in list[0]:
        list.clear()
        continue
    
    list.pop(0)
    entire_book.append(list)
    
driver.quit()

df = pd.DataFrame(entire_book, index=None, columns=['Title', 'Author'])
df.to_excel('temporary.xlsx')