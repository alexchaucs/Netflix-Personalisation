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


row_processed = {}
i = 0
while i not in row_processed:  
    row_processed[i] = "Yes"
    print(i)
    try:
        print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-1']/div[1]/a").get_attribute('aria-label'))
        try:
            print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-2']/div[1]/a").get_attribute('aria-label'))
            print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-3']/div[1]/a").get_attribute('aria-label'))
            print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-4']/div[1]/a").get_attribute('aria-label'))
            i += 1
        except:
            i += 1
            continue

    except:
        print("Scrolling")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        try:
            print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-1']/div[1]/a").get_attribute('aria-label'))
            try:
                print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-2']/div[1]/a").get_attribute('aria-label'))
                print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-3']/div[1]/a").get_attribute('aria-label'))
                print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-4']/div[1]/a").get_attribute('aria-label'))
                i += 1
            except:
                i += 1
                continue     
        except:
            time.sleep(5)
            try:
                print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-1']/div[1]/a").get_attribute('aria-label'))
                try:
                    print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-2']/div[1]/a").get_attribute('aria-label'))
                    print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-3']/div[1]/a").get_attribute('aria-label'))
                    print(driver.find_element_by_xpath("//*[@id='title-card-"+str(i)+"-4']/div[1]/a").get_attribute('aria-label'))
                    i += 1
                except:
                    i += 1
                    continue  
            except:
                print("Unable to Scroll Anymore")



# #374
# It Takes a Man and a Woman
# It Takes Two
# It's Complicated
# 375