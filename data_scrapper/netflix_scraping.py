import pandas as pd
import config ##config_example
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('./chromedriver')

### Extracting Netflix Australia Titles
netflix = "https://www.netflix.com/au/login"
driver.get(netflix)

driver.find_element_by_id("id_userLoginId").send_keys(config.username)
driver.find_element_by_id("id_password").send_keys(config.password)
driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div[3]/div/div/div[1]/form/button").click()
time.sleep(5)
driver.find_element_by_xpath("//*[@id='appMountPoint']/div/div/div[1]/div[1]/div[2]/div/div/ul/li[1]/div/a").click()
# driver.get("https://www.netflix.com/browse/genre/34399?so=az")
driver.get("https://www.netflix.com/browse/genre/34399?so=za")

