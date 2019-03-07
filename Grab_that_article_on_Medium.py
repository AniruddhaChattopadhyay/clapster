from selenium import webdriver
import time
import csv
from selenium.common.exceptions import TimeoutException
from collections import OrderedDict
from itertools import repeat
import winsound

def grab():
        driver = webdriver.Firefox()
        driver.get("https://medium.com/")
        driver.implicitly_wait(10)
        #action = webdriver.ActionChains(driver)
        time.sleep(2)

        login = driver.find_element_by_xpath("//*[@id=_obv.shell._surface_1551274578913]/div/div[1]/div[2]/div[2]/div/a[3]").click()
        login_google = driver.find_element_by_xpath('/html/body/div[4]/div/div/section/div[1]/div/button[1]').click()

        # You can log-in using google only
        print(" Logging in to Medium by using Google ")
        time.sleep(3)

        user = driver.find_element_by_xpath('//*[@id="identifierId"]')
        # Enter your email or phone number as registered in Medium
        user.send_keys('studyaniruddha@gmail.com') # Provide your email or registered phone number here

        nextButton = driver.find_element_by_xpath('//*[@id="identifierNext"]/content')
        nextButton.click()
        time.sleep(2)

        user = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')

        # Place just your password in the pass.txt file
        with open('pass.txt', 'r') as f:
            Password = f.read().replace('\n', '')
        user.send_keys(Password)

        LOG = driver.find_element_by_xpath('//*[@id="passwordNext"]/content').click()
        print('LOGIN SUCCESSFUL \n')

        topics = {
            0: 'Home',
            1: 'Technology',
            2: 'Culture',
            3: 'Entrepreneurship',
            4: 'Creativity',
            5: 'Self',
            6: 'Productivity',
            7: 'Design',
            8: 'Popular'
        }
        print('  Where would you like to dive in?  ')
        print(  """            0--> HOME\ \n
                    1-->TECHNOLOGY\ \n
                    2-->CULTURE \ \n
                    3-->ENTREPRENEURSHIP\ \n
                    4-->CREATIVITY\ \n
                    5-->SELF\ \n
                    6-->PRODUCTIVITY\ \n
                    7-->DESIGN \n
                    8-->POPULAR  """ )
        try:
            #topic = int(input())
            topic = 6
            output = 'You Chose ' + topics[topic]
            print(output)
        except:
            print('Select a valid topic')


        if topic == 0:
            t = driver.find_element_by_link_text('HOME').click()
        elif topic == 1:
            t = driver.find_element_by_partial_link_text('TECH').click()
        elif topic == 2:
            t = driver.find_element_by_partial_link_text('CULTURE').click()
        elif topic == 3:
            t = driver.find_element_by_partial_link_text('').click()
        elif topic == 4:
            driver.find_element_by_partial_link_text('MORE').click()
            time.sleep(1.5)
            t = driver.find_element_by_partial_link_text('CREATIVITY').click()
        elif topic == 5:
            t = driver.find_element_by_partial_link_text('SELF').click()
        elif topic == 6:
            driver.find_element_by_partial_link_text('MORE').click()
            time.sleep(5)
            t1 = driver.find_elements_by_tag_name('a')
            t = driver.find_element_by_partial_link_text('Productivity').click()
        elif topic == 7:
            t = driver.find_element_by_partial_link_text('DESIGN').click()
        elif topic == 8:
            t = driver.find_element_by_partial_link_text('POPULAR').click()
        else:
            print('Please select a correct topic.')

        print('The list of articles under this topic are saved as output.txt text file : ')
        # print('Just scan through the file and open the link whichever you want to read    :)  \n')
        print('The program is crawling down the webpage to gather links of around past 50 atricles. This may take around a minute or two.')

        # To Scroll to the bottom/ a portion of page
        last_height = 9000
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height >= last_height:
                break

        tag = driver.find_elements_by_tag_name('h3')

        unique_list = list(OrderedDict(zip(tag, repeat(None)))) # To remove duplicates from list

        tag = unique_list[1:52]
        tag_len = len(tag)
        print(tag_len)
        tag.pop(3)
        href = []

        for i in tag:
            href = href + [driver.find_element_by_link_text(i.text).get_attribute('href')]


        print(tag[0].text)
        print(href[0])

        with open('list.csv', 'w', newline='') as list_file:
            list_file = csv.writer(list_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            i = 0
            if tag_len > 0:
                while i < 50:
                    a = str(tag[i].text)
                    print(a)
                    list_file.writerow([i, a , str(href[i])])
                    i = i + 1


        """f= open("output.txt","w+") # Stores ouput in output.txt in the same file directory
        i=0
        if tag_len>0:
            while i<50:
                a = str(tag[i].text)
                print(a)
                f.write(time.strftime("%Y-%m-%d %H:%M") + '\n')
                f.write(a)
                f.write('\nLink is -->   ' + str(href[i])  + '\n\n')
                i = i+1"""

if __name__ == '__main__':
    grab()
