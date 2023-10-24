from selenium import webdriver
from selenium.webdriver.common.by import By
from icecream import ic

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR,".event-widget time")

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

upcoming_events = {}
n = 0
for time in event_times:
    # ic(time.text)
    upcoming_events[n] = {"time": time.text}
    n += 1

i = 0
for event in events:
    # ic(event.text)
    upcoming_events[i].update({"name": event.text})
    i += 1

ic(upcoming_events)

driver.close()