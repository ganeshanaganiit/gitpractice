import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import Logs

class Test_001:

    baseurl = ReadConfig.getapplicationurl()
    username = "admin@yourstore.com"
    password = "admin"
    logger = Logs.loggen()

    def test_login(self):

        self.logger.info("**********Test_001************")
        self.logger.info("*********Verifying_Title_of_the_Page************")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseurl)
        title = self.driver.title
        if title == "Your store. Login":
            assert True

        else:
            assert False
