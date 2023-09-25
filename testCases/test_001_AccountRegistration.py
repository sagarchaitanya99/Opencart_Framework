import os

from pageObjects.HomePage import Homepage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import randomString
from utilities.customlogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_AccountRegestration():
    baseurl= ReadConfig.getApplicationURL() #import from ReadProperties in utilities folder----common data
    logger = LogGen.loggen() #logs Purpose ------#notworking in pytest new versions

    def test_AccountRegister(self,setup):
        self.driver =setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.logger.info("****HomePage launched*****")
        self.Hp=Homepage(self.driver)
        self.Hp.click_My_account()
        self.Hp.click_Register()

        self.logger.info("****AccountRegestration started *****")
        self.RP = AccountRegistrationPage(self.driver)
        self.RP.setFirstName("johnn")
        self.RP.setLastName("visg")
        self.email = randomString.random_string_generator() + '@gmail.com'
        self.RP.setEmail(self.email)
        self.RP.setPassword("Sagar@12345")
        self.RP.setScroll()
        self.RP.setPrivacyPolicy()
        self.RP.clickContinue()
        self.RP.getconfirmationmsg()
        self.driver.close()



