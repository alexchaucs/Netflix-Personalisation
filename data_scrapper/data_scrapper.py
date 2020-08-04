import pandas as pd
import requests
from lxml import html
import config

url = "https://www.netflix.com/au/login"



session_requests = requests.session()
result = session_requests.get(login_url) 


print(config.username)
print(config.password)

#test