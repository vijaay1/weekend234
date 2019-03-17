from selenium import webdriver
#from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get("https://jqueryui.com/datepicker/#dropdown-month-year")
driver.maximize_window()
driver.implicitly_wait(30)
#val=driver.find_element_by_tag_name("iframe")
#driver.switch_to.frame(val)
#driver.find_element_by_id("datepicker").click()

month_val="7"
date_val="10"
year_val="2010"

ele=driver.find_element_by_xpath("//iframe[@class='demo-frame']")
driver.switch_to.frame(ele)
driver.find_element_by_id("datepicker").send_keys(month_val+"/"+date_val+"/"+year_val)
driver.find_element_by_id("datepicker").send_keys(Keys.ENTER)


#//*[@id='ui-datepicker-div']/table/tbody/tr[2]/td[1]/a[text()="4"]

# xp1="//*[@id='ui-datepicker-div']/table/tbody/tr/td/a[text()="
# xp2="'"
# xp3="'"
# xp4="]"
# fxp=xp1+xp2+date_val+xp3+xp4
# month=driver.find_element_by_class_name("ui-datepicker-month")
# m=Select(month)
# m.select_by_value(month_val)
#
# year=driver.find_element_by_class_name("ui-datepicker-year")
# yr=Select(year)
# yr.select_by_visible_text(year_val)
#  driver.find_element_by_xpath(fxp).click()