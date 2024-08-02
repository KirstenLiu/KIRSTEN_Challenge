from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

test_link = "https://localhost"

driver.get(test_link)

expected_title = "Hello World"
actual_title = driver.title

if actual_title == expected_title:
    print("Title validation passed.")
else:
    print("Title validation failed. Expected:", expected_title, "Actual:", actual_title)

element = driver.find_element(By.TAG_NAME, "h1")


expected_h1 = "Hello World!"

if element.text == expected_h1:
    print("Element validation passed.")
else:
    print("Element validation failed. Expected:", expected_h1, "Actual:", element)

driver.quit()