from selenium.webdriver.common.by import By


class Confirm:
    country=((By.CSS_SELECTOR,"#country"))
    india = ((By.LINK_TEXT,"India"))
    checkBox=((By.XPATH,"//label[@for='checkbox2']"))
    submit= ((By.CSS_SELECTOR,"input[class*='btn-success']"))
    successText=((By.CSS_SELECTOR,"div[class*='alert-success']"))
    def __init__(self,driver):
        self.driver=driver

    def getContry(self):
        # self.driver.find_element_by_css_selector("#country")
        return self.driver.find_element(*Confirm.country)
    def getIndia(self):
        # self.driver.find_element_by_xpath("India").click()
        return self.driver.find_element(*Confirm.india)
    def getCheckBox(self):
        # self.driver.find_element_by_xpath("//label[@for='checkbox2']")
        return self.driver.find_element(*Confirm.checkBox)
    def getSubmit(self):
        # self.driver.find_element_by_css_selector("input[class*='btn-success']")
        return self.driver.find_element(*Confirm.submit)
    def getSuccessText(self):
        # self.driver.find_element_by_css_selector("div[class*='alert-success']").click()
        return self.driver.find_element(*Confirm.successText)
