from selenium import webdriver
import ReuseChrome
from login_buess import Test01
from plan_buess import Test02


class Test(object):

    def __init__(self, base_url='http://tapd.oa.com/'):
        self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(r'C:\Users\v.liuxingwen\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.base_url = base_url
        self.driver.get(base_url)
        self.driver.implicitly_wait(30)

    def test01(self):
        step1 = Test01()
        step1.test_login(self.driver)
        step2 = Test02()
        step2.test_plan(self.driver)


tt = Test()
tt.test01()
