from selenium import webdriver
from selenium.webdriver.common.by import By
from icecream import ic

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://camelcamelcamel.com/product/B0B7RSV894")
# driver.get("https://www.amazon.com/gp/product/B0B7RSV894/ref=ox_sc_saved_title_6?smid=A3H3ISK374NPRT&th=1")

price = driver.find_element(By.CLASS_NAME, value="green").text
ic(price)

# Find Element by Name
# search_bar = driver.find_element(By.NAME, value="q")
# search_bar.tag_name #input
# search_bar.get_attribute("placeholder") #specific attribute

# Find Element by ID
# button = driver.find_element(By.ID, value="submit")
# button.size

# Find Element by CSS Selector
doc_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").text

# Find element by XPATH
link = driver.find_element(By.XPATH, value="/html/body/div[1]/div/div[6]/div[3]/div[4]/div[1]/div/h1")


# driver.close() #closes a tab
driver.quit() #closes entire browser