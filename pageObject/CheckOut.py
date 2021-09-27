from selenium.webdriver.common.by import By

from pageObject.Confirm import Confirm


class CheckOut:
    products=((By.XPATH,"//div[@class='card h-100']"))
    buttonCheckout=((By.CSS_SELECTOR,"a[class*='btn-primary']"))
    paymentCheckout=((By.CSS_SELECTOR,"button[class*='btn-success']"))
    def __init__(self,driver):
        self.driver=driver
    def getProducts(self):
        # self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        return self.driver.find_elements(*CheckOut.products)

    def getbuttonCheckout(self):
        # self.driver.find_element_by_css_selector("a[class*='btn-primary']")
        return self.driver.find_element(*CheckOut.buttonCheckout)

    def getpaymentCheckout(self):
        # self.driver.find_element_by_css_selector("button[class*='btn-success']")
        self.driver.find_element(*CheckOut.paymentCheckout).click()
        confirm = Confirm(self.driver)
        return confirm

