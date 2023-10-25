from selenium import webdriver
from selenium.webdriver.common.by import By
import json

driver = webdriver.Chrome()
driver.get("https://cookiesandcups.com/recipe-finder/?_search=cookies")


images = driver.find_elements(By.CLASS_NAME, 'wp-post-image')


image_data = []


for img in images:
    url = img.get_attribute("src")
    alt = img.get_attribute("alt")
    image_data.append({"url": url, "alt": alt})

image_data_json = json.dumps(image_data, indent=2)
print(image_data_json)

driver.quit()



