import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Use a raw string (r'') to handle backslashes in Windows
driver_path = r'C:\Users\renz dominic alib\PycharmProjects\Python_Selenium\Selenium_Python_Demo\chromedriver.exe'
service_obj = Service(driver_path)

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--headless')
chrome_opt.add_argument('--no-sandbox')
chrome_opt.add_argument('--disable-dev-shm-usage')
chrome_opt.add_argument('--disable-extensions')
chrome_opt.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=service_obj, options=chrome_opt)
# driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(3)
driver.find_element(By.XPATH, "//input[@name='username']").send_keys('Admin')
driver.find_element(By.XPATH, "//input[@name='password']").send_keys('wrongPW')
driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)
error_message = driver.find_element(By.XPATH, "//div[@role='alert']//p").text
print(error_message)
assert error_message == 'Invalid credentials'
