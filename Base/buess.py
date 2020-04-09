from time import sleep

from selenium.webdriver.common.by import By

from Base.page import SearchPage


class BaiDuSearch(object):

    def test_search(self):
        pic = By.ID, 'kw'
        enter = By.ID, 'su'
        s = SearchPage()
        s.send_pic(pic, 'selenium')
        s.click_pic(enter)
        sleep(3)
        s.quit()
