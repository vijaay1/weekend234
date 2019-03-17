from selenium import webdriver

driver=webdriver.Chrome()
driver.get("file:///E:/test/login.html")
driver.maximize_window()
#driver.implicitly_wait(30)
driver.find_element_by_id("").send_keys("")
driver.find_element_by_class_name("um").send_keys("password")
driver.find_element_by_id("login").click()
string()
print
#val1=driver.find_element_by_id("login").text
##print((val1))
# driver.quit()