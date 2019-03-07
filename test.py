from selenium import webdriver
import time
import csv
from urllib.request import urlopen
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from collections import OrderedDict
from itertools import repeat

def check_K(a):
    if a[-1:] == 'K' or a[-1:] == 'k':
        a = float(a[:-1])
        a = a*1000
        return a
    else:
        a = float(a)
        return a
def check_resp(a):
    if a[-1:] == 's':
        a = a[:-10]
        a = check_K(a)
        return a
    elif a[-1:] == 'e':
        a = a[:-9]
        return float(a)


href = ['']
with open('list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 2
    i=0
    for row in csv_reader:
        href = href + [str(row[2])]
href = href[1:51]

driver = webdriver.Firefox()
driver.get(href[24])
#print(href)

title = driver.find_element_by_class_name("readingTime").get_attribute('title')
print(title)

date = driver.find_element_by_tag_name('time')
print(date.text)

#/html/body/div[1]/div[2]/div/main/article/footer/div[1]/div[2]/div/div/ul
#/html/body/div[1]/div[2]/div/main/article/footer/div[2]/div/div/li/div[3]/h3/a

i=1
while(1):
    try:
        str1 = '/html/body/div[1]/div[2]/div/main/article/footer/div[1]/div[2]/div/div/ul/li[' + str(i) + ']/a'
        tag = driver.find_element_by_xpath(str1)
        print(tag.text)
        i += 1
    except:
        break

aut = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/main/article/footer/div[2]/div/div[1]/li/div[3]/h3/a')
print(aut.text)

"""--------------------------------------Author Page-----------------------------------------------------"""

driver.get(aut.get_attribute('href'))

time.sleep(1)

try:
    followers = driver.find_element_by_xpath('/html/body/div/div/section/div[1]/div[2]/div[2]/div[4]/span/div/div[2]/a')
except:
    followers = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[1]/a[2]/span')
else:
    pass


followers = str(followers.text)

if followers[-1:] == 's':
    followers = followers[:-10]

followers = check_K(followers)
print(followers)



try:
    following = driver.find_element_by_xpath('/html/body/div/div/section/div[1]/div[2]/div[2]/div[4]/span/div/div[1]/a')
except:
    following = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div[1]/a[1]/b')
else:
    pass


following = str(following.text)

if following[-1:] == 'g':
    following = following[:-10]

following = check_K(following)
print(following)

#/html/body/div/div/section/div[2]/div[1]/div[2]/div/span/div/div[2]
#/html/body/div/div/section/div[2]/div[1]/div[4]/div/span/div/div[2]



claps_a = []
responses_a = []
for i in range(1,1000):
    try:
        s = '/html/body/div/div/section/div[2]/div[1]/div[' + str(i) + ']/div/span/div/div[1]/div'
        s2 = '/html/body/div/div/section/div[2]/div[1]/div['+ str(i) +']/div/span/div/div[2]'
        claps_a = claps_a + [check_K(driver.find_element_by_xpath(s).text)]
        responses_a = responses_a + [check_resp(driver.find_element_by_xpath(s2).text)]
    except:
        pass
responses_b = [0 if x == None else x for x in responses_a]
print(claps_a)
print(responses_b)
with open('author.csv', 'a') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(title)