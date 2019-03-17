from selenium import webdriver

driver=webdriver.Chrome()
driver.get("http://localhost:8080/login?from=%2F")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element_by_id("j_username").send_keys("admin")
driver.find_element_by_name("j_password").send_keys("manager")
driver.find_element_by_name("Submit").click()
driver.find_element_by_xpath("//*[-()='log out']").click()