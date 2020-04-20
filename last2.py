
from selenium import webdriver
from time import sleep
from login_buess import *
from plan_buess import *


class CaseRun(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'http://tapd.oa.com'

    def test_search(self):
        change = By.CSS_SELECTOR, '.link_1'
        input_user = By.NAME, 'txtLoginName'
        input_pwd = By.NAME, 'txtPassword'
        enter = By.CSS_SELECTOR, '#ibnLogin'

        new_link = 'http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list'
        create_plan_button = By.CSS_SELECTOR, '.bug-list-head-btn-span'
        title_input = By.XPATH, '//*[@id="TestPlanName"]'

        lo = LoginPage(self.driver, self.url)
        lo.get_new_link(self.url)
        lo.click_button(change)
        lo.send_button(input_user, 'p_lxwenliu')
        lo.send_button(input_pwd, 'Morenpwd@159')
        lo.click_button(enter)
        lo.get_new_link('http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list')

        pl = PlanPage(self.driver, 'http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list')
        pl.click_button(create_plan_button)
        pl.exchange_handel()
        print('切换成功')
        pl.send_button(title_input, '这里是标题')
        # sleep(3)
        pl.quit()


c = CaseRun()
c.test_search()
