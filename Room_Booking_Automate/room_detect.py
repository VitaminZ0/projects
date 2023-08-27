from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import auth_key

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://libraryrooms.baruch.cuny.edu/spaces?lid=16857&gid=35704')

sleep(1)

while True:
    try:
        driver.find_element(By.CSS_SELECTOR,'[title="12:00pm Friday, September 1, 2023 - Room 452 - Available"]').click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.find_element(By.CSS_SELECTOR, '[value="2023-09-01 14:00:00"]').click()
        driver.find_element(By.ID, "submit_times").click()
        sleep(1)
        break

    except NoSuchElementException:
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Next"]').click()    
        sleep(2)
    

driver.find_element(By.ID, "username").send_keys(auth_key.email)
driver.find_element(By.ID, "password").send_keys(auth_key.password)
driver.find_element(By.NAME, "_eventId_proceed").click()

sleep(1)

driver.find_element(By.ID, "btn-form-submit").click()

sleep(180)

driver.quit()