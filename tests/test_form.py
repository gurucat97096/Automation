from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:8000/")

input_box = driver.find_element(By.NAME, "name")
input_box.send_keys("多多")

submit_btn = driver.find_element(By.CSS_SELECTOR, "input[type='submit']")
submit_btn.click()

time.sleep(1)

assert "Hello, 多多!" in driver.page_source
print("成功")

driver.quit()
