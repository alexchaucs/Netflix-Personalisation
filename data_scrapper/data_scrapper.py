import pandas as pd
import config ##config_example
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

### Extracting Netflix Australia Titles
url = "https://www.netflix.com/au/login"
driver.get(url)
