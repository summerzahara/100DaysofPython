from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from icecream import ic

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# ic(count.text)
# count.click()

all_portals = driver.find_element(By.LINK_TEXT, "Community portal")
# all_portals.click()

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search_1 = driver.find_element(By.NAME, "search")
search_1.send_keys(Keys.ENTER)

# driver.quit()