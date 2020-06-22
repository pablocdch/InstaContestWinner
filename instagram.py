import random
import openpyxl
import pyperclip
from selenium import webdriver
import time
import sys

username = "" #FILL USERNAME
password = "" #FILL PASSWORD
getdriver = ("https://www.instagram.com/accounts/login/")
contest = ("") #FILL CONTEST URL
driver = webdriver.Firefox()                                                        #opens firefox
driver.get(getdriver)                                                               #opens url login
time.sleep(5)                                                                       #timer to account for slow internet speed
driver.find_element_by_xpath("//input[@name='username']").send_keys(username)       #enters username
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)       #enters password
driver.find_element_by_css_selector(".L3NKy > div:nth-child(1)").click()            #clicks login
time.sleep(5)                                                                       #timer to account for slow internet speed
driver.get(contest)                                                                #goes to contest URL

wb = openpyxl.load_workbook('.xlsx') #FILL WORKBOOK FILENAME
sheet = wb['Sheet1']                                                                #activates sheet
n = 0                                                                               #set i to 0 to start counter

while n < 150:                                                                       #number of comments to comment.
    print('//////////////////LOG/////////////////')
    randNum = random.randint(0,13)                                                  #picks random number from 0 to 13, which is the comment to use for each i
    time_between_comments = random.randint(100,200)
    if randNum == 0:
        comment = sheet['A1']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 1:
        comment = sheet['A2']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 2:
        comment = sheet['A3']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 3:
        comment = sheet['A4']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 4:
        comment = sheet['A5']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 5:
        comment = sheet['A6']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 6:
        comment = sheet['A7']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 7:
        comment = sheet['A8']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 8:
        comment = sheet['A9']                                                       #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 9:
        comment = sheet['A10']                                                      #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 10:
        comment = sheet['A11']                                                      #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)
    elif randNum == 11:
        comment = sheet['A12']                                                      #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds.')
        time.sleep(time_between_comments)
    elif randNum == 12:
        comment = sheet['A13']                                                      #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds.')
        time.sleep(time_between_comments)
    elif randNum == 13:
        comment = sheet['A14']                                                      #selects comment
        pyperclip.copy(comment.value)                                               #copies comment
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        n = n + 1
        print('The number is ' + str(randNum) + ', and the comment is: ' + str(pyperclip.paste()))
        print('I will comment again in ' + str(time_between_comments) + ' seconds.')
        time.sleep(time_between_comments)
    else:
        print('Error')                                                              #In case of unexpected error
else:
    print('The number of comments specified has been reached.')
