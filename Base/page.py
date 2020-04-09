from time import sleep
from selenium.webdriver.common.by import By
from Base.base import BaseAction


class SearchPage(BaseAction):
    def send_pic(self, ele, text):
        self.send_button(ele, text)

    def click_pic(self, ele):
        self.click_button(ele)


if __name__ == '__main__':
    pic = By.ID, 'kw'
    enter = By.ID, 'su'
    s = SearchPage()
    s.send_pic(pic, 'selenium')
    s.click_pic(enter)
    sleep(3)
    s.quit()



