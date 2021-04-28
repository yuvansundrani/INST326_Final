from selenium import webdriver

from selenium.webdriver.common.keys import Keys

stringFromReddit = input("What would you like to search?: ")

driver = webdriver.Safari()
driver.get("https://www.target.com")
driver.maximize_window()

searchBox = driver.find_element_by_id("search")
searchBox.send_keys(stringFromReddit)

searchBox.send_keys(Keys.RETURN)

