
from selenium import webdriver
from time import sleep
from login_buess import *
from plan_buess import *
from login_buess import Test01
from plan_buess import Test02
from chose_buess import Test03
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class CaseRun(object):

    def __init__(self):
        # self.driver = webdriver.Chrome(r'C:\Users\v.liuxingwen\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.url = 'http://tapd.oa.com'
        # self.driver.minimize_window()
        # self.driver.maximize_window()
        # self.driver.set_window_size(width=1900, height=1400, windowHandle="current")
        from selenium.webdriver.chrome.options import Options
        chrome_options = Options()

        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'C:\Users\v.liuxingwen\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def test_search(self):

        lo = Test01()
        lo.test_login(self.driver, self.url)
        # print(lo.get_hand(self.driver))

        pl = Test02()
        pl.test_plan(self.driver, self.url)

        p2 = Test03()
        p2.test_chose(self.driver, self.url)


c = CaseRun()
c.test_search()
