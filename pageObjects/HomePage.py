import webdriver_manager
from selenium.webdriver.common.by import By

class Homepage():
    link_myaccount_xpath="//span[normalize-space()='My Account']"
    link_Register_xpath="//a[normalize-space()='Register']"
    link_login_xpath="//a[normalize-space()='Login']"


    def __init__(self,driver):
        self.driver=driver

    def click_My_account(self):
        self.driver.find_element(By.XPATH,self.link_myaccount_xpath).click()

    def click_Register(self):
        self.driver.find_element(By.XPATH,self.link_Register_xpath).click()

    def click_login(self):
        self.driver.find_element(By.XPATH,self.link_login_xpath).click()



