from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

service = Service(executable_path="chromedriver.exe")
options = webdriver.ChromeOptions()
# Add options to avoid detection
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(service=service, options=options)
# Remove webdriver property
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get("https://orteil.dashnet.org/cookieclicker/")

print("Waiting for page to load...")

# Wait for and click language selection
try:
    WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'English')]"))
    )
    language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
    language.click()
    print("Language selected")
    time.sleep(3)  # Give game time to initialize after language selection
except Exception as e:
    print(f"Language selection error (might already be set): {e}")

print("Please solve any CAPTCHA if it appears...")
print("Waiting 60 seconds before starting automation...")
time.sleep(60)  # Time to manually solve CAPTCHA

# Now wait for the cookie to be present and clickable
print("Waiting for game to fully load...")
WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.ID, "bigCookie"))
)

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

cookie = driver.find_element(By.ID, cookie_id)
print("Game loaded! Starting automation...")

while True:
    cookie.click()
    # Add small random delay to mimic human behavior
    time.sleep(random.uniform(0.01, 0.05))

    cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
    cookies_count = int(cookies_count.replace(",", ""))
    print(cookies_count)

    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")

        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)

        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break