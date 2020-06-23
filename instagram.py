import random, openpyxl, pyperclip, time, sys
from selenium import webdriver

class InstaWinner():
    username = ""
    password = ""
    contest = ("")
    sheet = ""
    driver = webdriver.Firefox()
    n = 0

    def __init__(self, *args, **kwargs):
        self.driver = webdriver.Firefox()                                                        #opens firefox
        print("Welcome to the Instagram Contest Winner.\nPlease fill the following info:")
        username = input("\n\nUsername: ")
        password = input("\nPassword: ")
        contest_url = input("\nContest URL: ")
        n = input("\nQuantity of comments to make: ")
        spread = input("\nSpreadsheet name: ")
        self.setUp(username,password,contest_url,n,spread)

    def setUp(self, username, password, contest_url, n, spread):
        self.username = username
        self.password = password
        self.contest = contest_url
        self.sheet = openpyxl.load_workbook(spread + '.xlsx')[0]
        self.n = n
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)                                                                       #timer to account for slow internet speed
        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(username)       #enters username
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(password)       #enters password
        self.driver.find_element_by_css_selector(".L3NKy > div:nth-child(1)").click()            #clicks login
        self.driver.get(self.contest)
        time.sleep(5)                                                                       #timer to account for slow internet speed
        self.work()

    def getRandomCommentContent(self):
        randNum = random.randint(0,13)                                                  #picks random number from 0 to 13, which is the comment to use for each i
        return [self.sheet['A' + str(randNum + 1)].value, str(randNum)]

    def postComment(self):
        print('//////////////////LOG/////////////////')
        time_between_comments = random.randint(100,200)
        comment = self.getRandomCommentContent()                                    #selects comment
        pyperclip.copy(comment[0])                                               #copies comment
        commentArea = self.driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.click()                                                         #click comment box
        commentArea = self.driver.find_element_by_class_name('Ypffh')                    #find comment box
        commentArea.send_keys(pyperclip.paste())                                    #pastes comment in comment box
        self.driver.find_element_by_css_selector("button.y3zKF:nth-child(2)").click()    #clicks post
        print('The number is ' + comment[1] + ', and the comment is: ' + comment[0])
        print('I will comment again in ' + str(time_between_comments) + ' seconds')
        time.sleep(time_between_comments)

    def work(self):
        i = 0
        while (i < self.n):
            self.postComment()
            i += 1
        print('The specified number of comments has been reached.')

iw = InstaWinner()