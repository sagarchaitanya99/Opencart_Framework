from  selenium.webdriver.common.by import By
import time


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_password_name = "password"
    btn_cont_xpath="//input[@value='Continue']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver



    def setFirstName(self,fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)


    def setPassword(self,pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setScroll(self):
        extra = self.driver.find_element(By.XPATH, "//h5[normalize-space()='Extras']")
        self.driver.execute_script("arguments[0].scrollIntoView(true)", extra)
        time.sleep(2)

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH, "//input[@name='agree']").click()
        time.sleep(2)


    def clickContinue(self):
        self.driver.find_element(By.XPATH,"//button[normalize-space()='Continue']").click()

    def getconfirmationmsg(self):
        try:
            return  self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None
