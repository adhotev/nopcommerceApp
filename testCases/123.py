import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service()
driver = webdriver.Chrome(service=s)

driver.get('https://admin-demo.nopcommerce.com/admin/')
driver.maximize_window()
driver.find_element(By.XPATH,"//button[normalize-space()='Log in']").click()
driver.find_element(By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]").click()
driver.find_element(By.XPATH, "//a[@class='btn btn-primary']").click()
# driver.find_element(By.XPATH, "//ul[@class='nav nav-pills nav-sidebar flex-column nav-legacy']/li[4]/a")
driver.find_element(By.XPATH, "//div[@class='input-group-append input-group-required']//div[@role='listbox']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[@title='delete']").click()
# driver.find_element(By.XPATH, "//ul[@id='SelectedCustomerRoleIds_listbox']/li[10]").click()
time.sleep(3)

