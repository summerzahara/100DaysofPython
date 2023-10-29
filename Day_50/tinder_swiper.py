import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from icecream import ic
from time import sleep
from dotenv import load_dotenv

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# Open Site
URL = "https://tinder.com/"
driver.get(URL)
sleep(3)


# Accept Cookies
cookies = driver.find_element(By.XPATH, "//*[@id='s1166637769']/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
ic(cookies.text)
cookies.click()
sleep(3)


# Sign In
login = driver.find_element(By.XPATH, "//*[@id='s1166637769']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
ic(login.text)
login.click()
sleep(10)

# Google Login
# google = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/span[1]")
# ic(google.text)
# sleep(5)

# Facebook Login
facebook = driver.find_element(By.XPATH, '//*[@id="s-561743307"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
ic(facebook.text)
facebook.click()
sleep(5)

# Phone Login
phone = driver.find_element(By.XPATH, "//*[@id='s-561743307']/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[3]/button/div[2]/div[2]/div/div")
ic(phone.text)
sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
ic(driver.title)

email = os.environ["FB_EMAIL"]
password = os.environ["FB_PASS"]

fb_email = driver.find_element(By.ID, "email")
fb_email.send_keys(email)
fb_password = driver.find_element(By.ID, "pass")
fb_password.send_keys(password)
fb_login = driver.find_element(By.NAME, "login")
ic(fb_login.text)
fb_login.click()
sleep(60)

driver.switch_to.window(base_window)
ic(driver.title)

#Allow location
allow_location = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location.click()

#Disallow notifications
notifications = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications.click()

#Allow cookies
cookies_2 = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies_2.click()