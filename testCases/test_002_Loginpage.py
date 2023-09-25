from pageObjects.HomePage import Homepage
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

import os

class Test_Login():
    baseURL = ReadConfig.getApplicationURL()

    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=Homepage(self.driver)
        self.hp.click_My_account()
        self.hp.click_login()

        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            assert False




