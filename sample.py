from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_link_text("Shop").click()
cards=driver.find_elements_by_css_selector("card-title")
i = -1
for card in cards:
    i = i + 1
    cardText = card.text
    print(cardText)
    if cardText == "Blackberry":
        driver.find_elements_by_css_selector("card-footer button")[i].click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
