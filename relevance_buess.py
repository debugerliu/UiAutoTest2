from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# from login_buess import *
from Base.base import GetWeekTime
from Pages.relevance_page import *


class Test04(object):

    # def get_handl(self, driver):
    #     qq = PlanPage(driver)
    #     ww = qq.print_handel()
    #     return ww

    # def __init__(self, driver):
    #     self.driver = driver

    def test_relevance(self, driver, url):
        global lo
        new_link = 'http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list'
        first_link = By.XPATH, '//*[@id="plan_list_contents"]/tbody/tr[1]/td[3]/a'
        go_button = By.XPATH, '//*[@id="id-tapd-toolbar"]/a[1]'
        links = By.XPATH, '//a[@class="story_name"]'
        # first_text = '//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[3]/div/div[1]/a[2]'

        lo = RelevancePage(driver)
        lo.click_button(first_link)
        lo.exchange_handel()
        lo.click_button(go_button)
            # get_text = lo.get_new_link_text(first_text)
            # all_links = 10
            # i = 1
            # while i < all_links:
            #     first_text = '//*[@id="test_plan_content"]/tbody[1]/tr['+str(i)+']/td[3]/div/div[1]/a[2]'
            #     get_text = lo.get_new_link_text(first_text)
            #     if '充值抽奖' in get_text:
            #         print('是一个充值抽奖活动')
            #         i += 1
            #     else:
            #         print('不是一个充值抽奖活动')
            #         i += 1
        link_list, elements = lo.get_every_text(links)
        print(link_list)
        lo.guanlian_test(links)
            # for i in link_list:
            #     if '充值抽奖' in i:
            #         print('是一个充值抽奖活动')
            #         lo
            #
            #     else:
            #         print('不是一个充值抽奖活动')
            # print(link_list)
            # for i in link_list:
            #     get_text = i.get
            #     sleep(2)
        lo.quit()
        # except Exception as e:
        #     lo.quit()
        #     print(e)


