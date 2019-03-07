from selenium import webdriver
import time
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from collections import OrderedDict
from itertools import repeat
import winsound
from Grab_that_article_on_Medium import grab


print(grab().href)
driver = webdriver.Firefox()
driver.get(href[0])
driver.implicitly_wait(10)
#action = webdriver.ActionChains(driver)
time.sleep(2)