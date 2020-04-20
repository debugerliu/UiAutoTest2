
from selenium import webdriver
from time import sleep
from login_buess import *
from plan_buess import *
from login_buess import Test01
from plan_buess import Test02
from chose_buess import Test03
from relevance_buess import Test04


class CaseRun(object):

    def __init__(self):
        self.driver = webdriver.Chrome(r'C:\Users\v.liuxingwen\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.url = 'http://tapd.oa.com'
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_search(self):

        lo = Test01()
        lo.test_login(self.driver, self.url)

        p1 = Test04()
        p1.test_relevance(self.driver, self.url)
        # print(lo.get_hand(self.driver))

        # pl = Test02()
        # pl.test_plan(self.driver, self.url)
        #
        # p2 = Test03()
        # p2.test_chose(self.driver, self.url)


c = CaseRun()
c.test_search()
