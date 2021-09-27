from selenium.webdriver.common.by import By

from pageObject.CheckOut import CheckOut


class HomePage:
    shop=((By.LINK_TEXT,"Shop"))
    name = ((By.NAME,"name"))
    nameLabel=((By.XPATH,"//label[text()='Name']"))
    email = ((By.NAME,"email"))
    emailLabel=((By.XPATH,"//label[text()='Email']"))
    password=((By.ID,"exampleInputPassword1"))
    checkBox=((By.ID,"exampleCheck1"))
    genderSelection=((By.ID,"exampleFormControlSelect1"))
    studentDetail=((By.ID,"inlineRadio2"))
    employDetail=((By.CLASS_NAME,"form-control"))
    success=((By.CLASS_NAME,"btn-success"))
    successText=((By.CSS_SELECTOR,"div[class*='alert-success']"))

    def __init__(self,driver):
        self.driver = driver

    def getShop(self):
        # self.driver.find_element_by_link_text("Shop")
        self.driver.find_element(*HomePage.shop).click()
        checkout = CheckOut(self.driver)
        return checkout
    def getName(self):
        # self.driver.find_element_by_name("name")
        return self.driver.find_element(*HomePage.name)
    def getNameLabel(self):
        # self.driver.find_element_by_xpath("//label[text()='Name']")
        return self.driver.find_element(*HomePage.nameLabel)
    def getEmail(self):
        # self.driver.find_element_by_name("email")
        return self.driver.find_element(*HomePage.email)
    def getEmailLabel(self):
        # self.driver.find_element_by_xpath("//label[text()='Email']")
        return self.driver.find_element(*HomePage.emailLabel)
    def getPassword(self):
        # self.driver.find_element_by_id("exampleInputPassword1")
        return self.driver.find_element(*HomePage.password)
    def getCheckBox(self):
        # self.driver.find_element_by_id("exampleCheck1")
        return self.driver.find_element(*HomePage.checkBox)
    def getGenderSelection(self):
        # self.driver.find_element_by_id("exampleFormControlSelect1")
        return self.driver.find_element(*HomePage.genderSelection)
    def getStudentDatail(self):
        # self.driver.find_element_by_id("inlineRadio2")
        return self.driver.find_element(*HomePage.studentDetail)
    def getEmployDatail(self):
        # self.driver.find_element_by_class_name("form-control")
        return self.driver.find_element(*HomePage.employDetail)
    def getSuccess(self):
        # self.driver.find_element_by_class_name("btn-success")
        return self.driver.find_element(*HomePage.success)
    def getSuccessText(self):
        # self.driver.find_element_by_css_selector("div[class*='alert-success']")
        return self.driver.find_element(*HomePage.successText)