from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

#Working With the radio butttons

driver.get("https://www.html.am/html-codes/forms/html-radio-button-code.cfm")

status = driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()     #false
print(status)

driver.find_element_by_id("RESULT_RadioButton-8_0").click()

status = driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()     #false/ true
print(status)

#Working With the check butttons

driver.find_element_by_id("RESULT_CheckBox-9_0").click()
driver.find_element_by_id("RESULT_CheckBox-9_6").click()

status = driver.find_element_by_id("RESULT_CheckBox-9_0").is_selected()
print(status)