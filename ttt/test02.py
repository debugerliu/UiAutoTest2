from time import sleep

from selenium.webdriver.common.by import By

from Pages.login_page import LoginPage


class Test01(object):

    def lognin(self):
        change = By.CSS_SELECTOR, '.link_1'
        input_user = By.NAME, 'txtLoginName'
        input_pwd = By.NAME, 'txtPassword'
        enter = By.CSS_SELECTOR, '#ibnLogin'
        lo = LoginPage()
        lo.click_button(change)
        lo.send_button(input_user, 'p_lxwenliu')
        lo.send_button(input_pwd, 'Morenpwd@159')
        lo.click_button(enter)
        lo.quit()
        print('成功了')


if __name__ == '__main__':
    s = Test01()
    s.lognin()

