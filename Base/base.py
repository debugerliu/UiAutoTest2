import datetime
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

import xlrd
from selenium import webdriver


# 创建基础类，之后的page需要基础此进行
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):

    # def __init__(self, driver):
    #     self.driver = driver

    # 初始化浏览器， 如需要修改url，则需要重写init并提供url
    def __init__(self,  driver, base_url='http://tapd.oa.com/'):
        # self.driver = webdriver.Chrome(r'C:\Users\v.liuxingwen\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        self.driver = driver
        self.base_url = base_url

    # def find_element(self, ele):
    #     return self.driver.find_element(ele[0], ele[1])

    def find_element(self, ele):
        return WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((ele[0], ele[1])))

    def find_elements(self, ele):
        return self.driver.find_elements(ele[0], ele[1])

    def get_every_text(self, ele):
        elements = self.find_elements(ele)
        ww = len(elements)
        print(ww)
        tt_list = []
        i = 0
        while i < ww:
            tt = elements[i].text
            i += 1
            # print(tt)
            tt_list.append(tt)
        print(tt_list)
        return tt_list, elements
        # for ele in elements:
        #     print(ele.text)

    def guanlian_test(self, ele1):
        chos = By.XPATH, '//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[2]/div/div'
        guanlian = By.XPATH, '//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[2]/div/div/div/div/ul/li[1]/a'
        threechose = By.XPATH, '//*[@id="ChooseTcaseKDialog_tree_3_switch"]'
        fivechose = By.XPATH, '//*[@id="ChooseTcaseKDialog_tree_5_switch"]'
        fourtingchose = By.XPATH, '//*[@id="ChooseTcaseKDialog_tree_14_check"]'
        sub_bu = By.XPATH, '//*[@id="-wrapper"]/div[3]/div/a[1]/span'
        title_bu = By.CSS_SELECTOR, 'a[class="story_name"]'

        title_list = self.find_elements(title_bu)

        l1, l2 = self.get_every_text(ele1)
        for i, l, ll in zip(l1, range(1, 10), range(10)):
            if '充值抽奖' in i:
                # self.mouser_fu('//*[@id="test_plan_content"]/tbody[1]/tr['+str(l)+']/td[2]/div/div/div')
                sleep(2)
                # self.mouser_fu('//*[@id="test_plan_content"]/tbody[1]/tr['+str(l)+']/td[3]/div/div[1]/a[2]')
                self.mouser_xuan(title_list[ll])
                sleep(3)
                # self.click_button('//*[@id="test_plan_content"]/tbody[1]/tr['+str(l)+']/td[2]/div/div/div')
                # self.click_button('//*[@id="test_plan_content"]/tbody[1]/tr['+str(l)+']/td[2]/div/div/div/a/i')
                # '//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[2]/div/div'
                # self.click_button('//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[2]')
                # self.click_button('//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[2]/div')
                self.click_button(chos)
                sleep(0.5)
                self.click_button(guanlian)
                sleep(0.5)
                self.click_button(threechose)
                sleep(0.5)
                self.click_button(fivechose)
                sleep(0.5)
                self.click_button(fourtingchose)
                sleep(0.5)
                self.click_button(sub_bu)
                sleep(2)
            else:
                continue


    # 点击方法的封装，find_element为定位方法，ele为传入的参数，需要使用下标取值
    def click_button(self, ele):
        self.find_element(ele).click()

    # 传参方法的封装，需要元素位置，和文本内容
    def send_button(self, ele, text):
        self.find_element(ele).send_keys(text)

    # def get_link(self, link):
    #     self.driver.get(link)

    def exchange_handel(self):
        now_handel = self.driver.current_window_handle
        all_handel = self.driver.window_handles
        for i in all_handel:
            if i != now_handel:
                self.driver.switch_to.window(i)
                return self.driver

    def print_handel(self):
        return self.driver.window_handles

    def exchange_three_handele(self, i):
        self.driver.switch_to.window(i)

    def get_driver_cookie(self):
        coo = self.driver.get_cookies()
        return coo

    def add_driver_cookie(self, cc):
        self.driver.add_cookie(cookie_dict=cc)

    def fanhui(self):
        return self.driver

    def close_handle(self):
        now_handel = self.driver.current_window_handle
        all_handel = self.driver.window_handles
        for i in all_handel:
            if i == now_handel:
                self.driver.switch_to.window(i)
                self.driver.close()

    def mouser_fu(self, ele):
        move = self.driver.find_element_by_xpath(ele)
        ActionChains(self.driver).move_to_element(move).perform()

    def mouser_xuan(self, move):
        ActionChains(self.driver).move_to_element(move).perform()

    def clean_form(self, ele):
        self.driver.find_element_by_name(ele).clear()

    def new_click(self, ele):
        dd = self.driver.find_element(ele)
        self.driver.execute_script("arguments[0].click();", dd)

    def get_link_text(self, ele):
        dd = self.driver.find_element_by_xpath(ele)
        ww = dd.text
        return ww

    def quit(self):
        self.driver.quit()


# 返回日期的方法
class GetWeekTime(object):

    def get_current_week(self):
        monday, sunday = datetime.date.today(), datetime.date.today()
        one_day = datetime.timedelta(days=1)
        while monday.weekday() != 0:
            monday -= one_day
        while sunday.weekday() != 4:
            sunday += one_day

        return monday, sunday


# 返回新数据的方法
class FormData(object):

    def __init__(self):
        pass

    def getinfos(self):
        data = xlrd.open_workbook(r'C:\Users\v.liuxingwen\PycharmProjects\myselenium2\Base\formdata.xls')
        # import sys
        # print(sys.argv[0])
        # 拿到句柄
        table = data.sheet_by_name('第一页')
        return table
        # 打印工作表
        # print(data.sheet_names())
        # # 行数
        # print(table.nrows)
        # # 列数
        # print(table.ncols)

    def getn(self):
        tt = self.getinfos()
        xxx = []
        num_list = tt.col_values(0)
        for i in num_list:
            if i != '':
                xxx.append(int(i))
        return xxx

    def getnn(self):
        xx = self.getn()
        print(len(xx))
        return xx


# if __name__ == '__main__':
#     cc = FormData()
#     for i in cc.getn():
#         print(i)