76from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://azure.microsoft.com/en-us/")
driver.maximize_window()
driver.implicitly_wait(30)
# driver.execute_script("window.scrollBy(0,5000)","")


# ele=driver.find_element_by_xpath("//h3[text()='DevOps']")
# driver.execute_script("arguments[0].scrollIntoView();",ele)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight):")
