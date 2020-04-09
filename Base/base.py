from selenium import webdriver


# 创建基础类，之后的page需要基础此进行
class BaseAction(object):

    # 初始化浏览器， 如需要修改url，则需要重写init并提供url
    def __init__(self,  base_url='http://www.baidu.com'):
        self.driver = webdriver.Chrome()
        self.base_url = base_url
        self.driver.get(base_url)

    # 点击方法的封装，find_element为定位方法，ele为传入的参数，需要使用下标取值
    def click_button(self, ele):
        self.driver.find_element(ele[0], ele[1]).click()

    # 传参方法的封装，需要元素位置，和文本内容
    def send_button(self, ele, text):
        self.driver.find_element(ele[0], ele[1]).send_keys(text)

    def quit(self):
        self.driver.quit()




