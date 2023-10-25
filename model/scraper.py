import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://cookiesandcups.com/recipe-finder/?_search=cookies")


imgs = driver.find_element(By.XPATH, '//*[@id="post-22335"]/div/div/div[1]/div/a/img')
url = imgs.get_attribute("src")
print(url)
driver.quit()
