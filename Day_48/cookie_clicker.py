from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from icecream import ic
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# time.sleep(5)
# language = driver.find_element(By.ID, "langSelect-EN")
# language.click()

cookie = driver.find_element(By.ID, "cookie")
money = driver.find_element(By.ID, "money")
my_money = int(money.text)
store = driver.find_elements(By.CSS_SELECTOR, "#store div b")

store.reverse()
store.pop(0)

for item in store:
    ic(item.text)

def buy_upgrade():
    for item in store:
        new_item = item.text.split()
        # ic(new_item)
        if my_money >= int(new_item[-1].replace(',', '')):
            ic(item)
            item.click()
            break



play = False
while play:
    cookie.click()
    if time.time() > timeout:
        buy_upgrade()


