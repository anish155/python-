from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://quotes.toscrape.com/js/")
time.sleep(2)


quotes = driver.find_elements(By.CLASS_NAME, "text")
for i, q in enumerate(quotes, 1):
    print(f"{i}. {q.text}")

driver.quit()
