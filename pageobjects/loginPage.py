from selenium import webdriver
class login:

    textbox_username_xpath= "//input[@id='Email']"
    textbox_password_xpath= "//input[@id='Password']"
    submit_button_xpath= "//button[@type='submit']"

    def __int__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def setButton(self, button):
        self.driver.find_element_by_xpath(self.submit_button_xpath).click()
        



    