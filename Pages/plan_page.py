from selenium.webdriver.common.by import By

from Base.base import BaseAction


class PlanPage(BaseAction):

    new_link = 'http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list'
    create_plan_button = By.CSS_SELECTOR, 'bug-list-head-btn-span'
    title_input = By.CSS_SELECTOR, '.invalid'

    def __init__(self, driver, base_url='http://tapd.oa.com/'):
        self.driver = driver

    def send_user(self, ele, text):
        self.send_button(ele, text)

    def submit_enter(self, ele):
        self.click_button(ele)

    def get_new_link(self, link):
        self.driver.get_link(link)

    def new_click(self, ele):
        self.click_button(ele)

    def new_submit(self, ele):
        self.new_click(ele)


