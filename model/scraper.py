from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cookiesandcups.com/recipe-finder/?_search=cookies")

images = driver.find_elements(By.CLASS_NAME, 'wp-post-image')

for img in images:
    url = img.get_attribute("src")
    print(url)

driver.quit()