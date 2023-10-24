import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from icecream import ic
import time
from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open Site
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3727925123&f_AL=true&geoId=90000084&keywords=technical%20program%20manager&location=San%20Francisco%20Bay%20Area&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true"
driver.get(URL)

# Sign In
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
ic(sign_in.text)
sign_in.click()

EMAIL = os.environ["LI_USERNAME"]
PASS = os.environ["LI_PASS"]

email = driver.find_element(By.ID, "username")
email.send_keys(EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASS)
submit = driver.find_element(By.CLASS_NAME, "btn__primary--large")
submit.click()
time.sleep(5)

# Select Job to Apply
easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button span")
ic(easy_apply.text)
easy_apply.click()
time.sleep(5)

next = driver.find_element(By.CSS_SELECTOR, "form footer div button span")
ic(next.text)
next.click()
time.sleep(5)

review = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary span")
ic(review.text)
review.click()
time.sleep(5)

submit = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary span")
ic(submit.text)
submit.click()