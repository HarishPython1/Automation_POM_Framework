class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.un_txt_bx_name='username'
        self.pwd_txt_bx_name='pwd'
        self.login_btn_xpath="//*[text()='Login ']"

    def enter_user_name(self):
        self.driver.find_element_by_name(self.un_txt_bx_name).send_keys("admin")

    def enter_password(self):
        self.driver.find_element_by_name(self.pwd_txt_bx_name).send_keys("manager")

    def click_on_login_btn(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()
