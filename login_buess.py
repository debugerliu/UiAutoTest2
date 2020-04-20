from time import sleep

from selenium.webdriver.common.by import By

from Pages.login_page import LoginPage


class Test01(object):

    def get_hand(self, driver):
        lo = LoginPage(driver)
        ww = lo.print_handel()
        return ww

    def test_login(self, driver, url):

        change = By.CSS_SELECTOR, '.link_1'
        input_user = By.NAME, 'txtLoginName'
        input_pwd = By.NAME, 'txtPassword'
        enter = By.CSS_SELECTOR, '#ibnLogin'

        lo = LoginPage(driver)
        lo.get_new_link(url)
        lo.click_button(change)
        lo.send_button(input_user, '')
        lo.send_button(input_pwd, '')
        lo.click_button(enter)
        lo.get_new_link('http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list')
        # han1 = lo.print_handel()
        # print(han1)
        # return han1
        # change = By.CSS_SELECTOR, '.link_1'
        # input_user = By.NAME, 'txtLoginName'
        # input_pwd = By.NAME, 'txtPassword'
        # enter = By.CSS_SELECTOR, '#ibnLogin'
        # lo = LoginPage(driver)
        # lo.click_button(change)
        # lo.send_button(input_user, 'p_lxwenliu')
        # lo.send_button(input_pwd, 'Morenpwd@159')
        # lo.click_button(enter)
        # print('成功了')
        # lo.get_new_link('http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list')
        # return lo.fanhui()


if __name__ == '__main__':
    s = Test01()
    s.test_login()

