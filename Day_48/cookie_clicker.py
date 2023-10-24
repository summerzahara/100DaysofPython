from selenium import webdriver
from selenium.webdriver.common.by import By
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

# Find the cookie
cookie = driver.find_element(By.ID, "cookie")

# Check for upgrades
store = driver.find_elements(By.CSS_SELECTOR, "#store div b")

store.reverse()
store.pop(0)

# list of items and prices
prices = [item.text.split('-') for item in store]
for item in prices:
    item[0] = item[0].strip()
    item[1] = int(item[1].strip().replace(",", ""))
ic(prices)


def buy_upgrade():
    # Check Money Available
    money = driver.find_element(By.ID, "money").text
    my_money = int(money.replace(",", ""))
    ic(my_money)

    for item in prices:
        if my_money >= item[1]:
            buy_id = f"buy{item[0]}"
            upgrade = driver.find_element(By.ID, buy_id)
            upgrade.click()
            break

buy_upgrade()

# Timers
five_sec = time.time() + 5
five_min = time.time() + 300

play = True
while play:
    cookie.click()
    if time.time() > five_sec:
        buy_upgrade()
        five_sec = time.time() + 5


    if time.time() > five_min:
        cps = driver.find_element(By.ID, "cps").text
        ic(cps)
        break


