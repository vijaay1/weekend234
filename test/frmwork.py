from selenium import webdriver
import time
def test_launch_url():
    global driver
    driver=webdriver.Firefox(executable_path="E:\\driver\\geckodriver-v0.24.0-win32 (1)\\geckodriver.exe")
    driver.get("http://localhost:8080/login?from=%2F")
    driver.maximize_window()
    driver.implicitly_wait(30)

def test_login():
    driver.find_element_by_name("j_username").send_keys("admin")
    driver.find_element_by_name("j_password").send_keys("manager")
    driver.find_element_by_name("Submit").click()

def test_logout():
    time.sleep()
    driver.find_element_by_xpath("//*[text()='log out']").click()
