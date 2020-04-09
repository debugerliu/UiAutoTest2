from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
e1 = driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span')
e2 = driver.find_element_by_xpath('//*[@id="form"]/span[1]/span')
print(e1)
print(e2)
