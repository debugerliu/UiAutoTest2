from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.plan_page import *
from login_buess import *
from Base.base import GetWeekTime


class Test02(object):

    def get_handl(self, driver):
        qq = PlanPage(driver)
        ww = qq.print_handel()
        return ww

    # def __init__(self, driver):
    #     self.driver = driver

    def test_plan(self, driver, url):
        global lo
        new_link = 'http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list'
        create_plan_button = By.CSS_SELECTOR, '.bug-list-head-btn-span'
        title_input = By.XPATH, '//*[@id="TestPlanName"]'
        status = By.XPATH, '//*[@id="TestPlanStatus"]'
        open_chose = By.XPATH, '//td[@title="开启"]'
        # open_chose = By.XPATH, '/html/body/div[3]/div[2]/table/tbody/tr[2]/td'
        start_time = By.XPATH, '//*[@id="TestPlanStartDate"]'
        end_time = By.XPATH, '//*[@id="TestPlanEndDate"]'
        test_type = By.XPATH, '//*[@id="TestPlanType"]'
        test_type_name = By.CSS_SELECTOR, '[value="功能测试"]'
        # submit_button = By.CSS_SELECTOR, '#btn_save_return'
        submit_button = By.XPATH, '//*[@id="btn_save_return"]'
        # submit_button = By.XPATH, '//*[@id="btn_save_return"]'

        plan_button = By.XPATH, '//*[@id="plan_list_contents"]/tbody/tr[1]/td[3]/a'
        name1 = By.XPATH, '//*[@id="TestPlanOwnerValue"]'
        go_button = By.XPATH, '//*[@id="id-tapd-toolbar"]/a[1]'

        # try:
        weektime = GetWeekTime().get_current_week()
        lo = PlanPage(driver)
        lo.click_button(create_plan_button)
        lo.exchange_handel()
        # 输入名称
        # lo.send_button(title_input, '白牌活动'+str(weektime[0]+'--'+str(weektime[1])))
        lo.send_button(title_input, '白牌活动'+str(weektime[0])+'————'+'白牌活动'+str(weektime[1]))
        lo.click_button(status)
        lo.click_button(open_chose)
        lo.send_button(start_time, str(weektime[0]))
        lo.send_button(end_time, str(weektime[1]))
        lo.click_button(title_input)
        lo.click_button(test_type)
        lo.click_button(test_type_name)
        lo.send_button(name1, 'p_lxwenliu(刘兴文);')
        lo.send_button(name1, 'p_wfangyuan(袁文芳);')
        lo.click_button(title_input)
        lo.click_button(submit_button)
        # lo.send_button(submit_button, Keys.ENTER)
        # lo.new_submit(submit_button)
        print(self.get_handl(driver))
        lo.click_button(plan_button)
        print(self.get_handl(driver))
        hans = self.get_handl(driver)[2]
        lo.exchange_three_handele(hans)
        lo.click_button(go_button)
        # except Exception as e:
        #     lo.quit()
        #     print(e)
