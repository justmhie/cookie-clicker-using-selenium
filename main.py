from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service) 

driver.get("https://www.google.com")

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("NASA Space Apps Challenge Davao" + Keys.ENTER)

WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "a h3"))
)

# Click the first search result title (h3 inside an anchor)
result = driver.find_element(By.CSS_SELECTOR, "a h3")
result.click()

# Click the chosen text
# link = driver.find_element(By.PARTIAL_LINK_TEXT, "Davao City")
# link.click()

time.sleep(30)

driver.quit()