
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObject.CheckOut import CheckOut
from pageObject.Confirm import Confirm
from pageObject.HomePage import HomePage
from utilities.BaceClass import BaseClass


class Test_end_to_end(BaseClass):
    def test_endToEnd(self):
        log=self.getLogger()
        homePage=HomePage(self.driver)
        checkout=homePage.getShop()
        log.info("getting all the product titles")
        products = checkout.getProducts()
        assert len(products) == 4
        for product in products:
            productName = product.find_element_by_xpath("div/h4/a").text
            log.info(productName)
            if productName == "Nokia Edge":
                product.find_element_by_xpath("div[2]/button").click()
                # driver.find_element_by_xpath("//div[@class='card h-100']/div[2]/button").click()
        checkout.getbuttonCheckout().click()
        confirm=checkout.getpaymentCheckout()
        log.info("entering country name as ind")
        confirm.getContry().send_keys("ind")
        self.verifyLinkPrecence("India")
        confirm.getIndia().click()
        confirm.getCheckBox().click()
        confirm.getSubmit().click()
        log.info("Text received from the application is "+confirm.getSuccessText().text)
        assert "Success" in confirm.getSuccessText().text
        self.driver.get_screenshot_as_file("screen.png")
        print("The frame work is completed")
