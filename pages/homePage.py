from selenium import webdriver

driver=webdriver.Chrome(executable_path="c:/chromedriver.exe")
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element_by_xpath("//div[@class='navigation clearfix']//a[contains(text(),'Practice Projects')]").click()
driver.find_element_by_css_selector("#name").send_keys("ARUN")
driver.find_element_by_css_selector("#email").send_keys("chanalarun@gmail.com")