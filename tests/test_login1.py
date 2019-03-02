import time
import os
from selenium import webdriver
import pytest
path1 = os.getcwd().replace("tests","").replace("\\","/")+"drivers/chromedriver.exe"
print(path1)

class TestLogin:
    @pytest.fixture(scope='class')
    def test_launch_browser(self):
        global driver
        driver=webdriver.Chrome(executable_path="C:/Users/QSP/PycharmProjects/Automation_POM_Framework/drivers/chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("http://localhost/login.do")

    def test_login(self,test_launch_browser):
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("pwd").send_keys("manager")
        driver.find_element_by_xpath("//*[text()='Login ']").click()

    def test_logout(self,test_launch_browser):
        time.sleep(5)
        driver.find_element_by_xpath("//*[text()='Logout']").click()

