from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

search = input("Enter search term: ")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")

search_box.send_keys(search)
search_box.send_keys(Keys.RETURN)

input("Press Enter to close browser...")

driver.quit()