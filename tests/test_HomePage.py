import pytest
from selenium.webdriver.support.select import Select

from pageObject.HomePage import HomePage
from testData.test_HomePageData import TestHomePageData

from utilities.BaceClass import BaseClass


class Test_HomePage(BaseClass):

    def test_HomePage(self,getData):
        log=self.getLogger()

        homePage=HomePage(self.driver)
        log.info("first name is "+getData["firstName"])
        homePage.getName().send_keys(getData["firstName"])
        nameLabel = homePage.getNameLabel().text
        assert nameLabel == "Name"
        homePage.getEmail().send_keys(getData["mail"])
        emailLabel = homePage.getEmailLabel().text
        assert emailLabel == "Email"
        homePage.getPassword().send_keys("shetty")
        homePage.getCheckBox().click()
        # select class is provide the methods to handle the option in dropdown
        self.selectOptionByText(homePage.getGenderSelection(),getData["gender"])

        homePage.getEmployDatail().click()
        # driver.find_element_by_class_name("form-control").send_keys("27/10/1991")
        homePage.getEmployDatail().click()
        homePage.getSuccess().click()
        successText = homePage.getSuccessText().text
        assert "Success" in successText
        self.driver.refresh()
    @pytest.fixture(params=TestHomePageData.test_Home_Page_Data)
    def getData(self,request):
        return request.param