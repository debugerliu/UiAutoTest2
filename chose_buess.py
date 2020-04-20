from time import sleep
from selenium.webdriver.common.by import By
from Pages.choose_page import ChoosePage
from login_buess import *
from Base.base import *



class Test03(object):

    def test_chose(self, driver, url):
        global lo
        new_link = 'http://tapd.oa.com//oppohuaweiui/sparrow/test_plan/plan_list'
        choose_button = By.CSS_SELECTOR, '.choose_story_handle'
        mouser_button = '//*[@id="subject-content"]/div[2]/div/div[1]/div[1]/div[1]/span'
        choose_xuqiu = By.XPATH, '//*[@id="subject-content"]/div[2]/div/div[1]/div[1]/div[1]/div/ul/li[2]/a'
        form_input = By.NAME, 'data[BasicSearch][id]'
        form_input_clear = 'data[BasicSearch][id]'
        filter_button = By.XPATH, '//*[@id="filter_submit"]'
        submit_button = By.XPATH, '//*[@id="kdialog_list"]/table/tbody/tr[1]/td[1]/input'
        more_chose = By.CSS_SELECTOR, '.more-filters'
        chose_id = By.CSS_SELECTOR, '[value="id"]'
        submit2_button = By.XPATH, '//*[@id="-wrapper"]/div[2]/div/a[1]/span'
        submit3_button = By.XPATH, '//*[@id="-wrapper"]/div[3]/div/a[1]/span'

        try:
            lo = ChoosePage(driver)
            lo.click_mouse_button(mouser_button)
            print('悬浮结束')
            lo.click_button(choose_xuqiu)
            lo.click_button(more_chose)
            lo.click_button(chose_id)
            lo.click_button(submit2_button)
            form_handel = FormData()
            formdata = form_handel.getn()
            ww = form_handel.getnn()[0]
            ii = 0
            for one in formdata:
                ii += 1
                lo.clean_form(form_input_clear)
                lo.send_button(form_input, one)
                lo.click_button(filter_button)
                sleep(0.2)
                lo.click_button(submit_button)
                if ii > ww:
                    break
            lo.click_button(submit3_button)
            lo.quit()
        except Exception as e:
            print(e)
            lo.quit()



