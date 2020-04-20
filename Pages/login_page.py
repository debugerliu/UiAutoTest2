from selenium.webdriver.common.by import By

from Base.base import BaseAction


class LoginPage(BaseAction):

    change = By.CSS_SELECTOR, '.link_1'
    input_user = By.NAME, 'txtLoginName'
    input_pwd = By.NAME, 'txtPassword'
    enter = By.CSS_SELECTOR, '#ibnLogin'

    # def __init__(self, driver, base_url='http://tapd.oa.com/'):
    #     self.driver = driver

    def send_user(self, ele, text):
        self.send_button(ele, text)

    def submit_enter(self, ele):
        self.click_button(ele)

    def get_new_link(self, link):
        self.driver.get(link)
