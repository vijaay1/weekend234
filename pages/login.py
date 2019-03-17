class Loginpage1:
    def __init__(self,driver):
        self.driver=driver
        self.un='j_username'
        self.pwd='j_password'
        self.submit='Submit'
    def enter_un(self):
        self.driver.find_element_by_name(self.un).send_keys("admin")

    def pwd_un(self):
        self.driver.find_element_by_name(self.pwd).send_keys("manager")

    def sub(self):
        self.driver.find_element_by_name(self.submit).click()