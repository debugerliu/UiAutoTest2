# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# e1 = driver.find_element(By.XPATH, '//*[@id="form"]/span[1]/span')
# e2 = driver.find_element_by_xpath('//*[@id="form"]/span[1]/span')
# print(e1)
# print(e2)

# import datetime
#
#
# def get_current_week():
#     monday, sunday = datetime.date.today(), datetime.date.today()
#     one_day = datetime.timedelta(days=1)
#     while monday.weekday() != 0:
#         monday -= one_day
#     while sunday.weekday() != 6:
#         sunday += one_day
#
#     return monday, sunday
#
#
# x = get_current_week()
# print(x[0])
# print(x[1])
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# cc = driver.get_cookies()
# print(cc)

# list22 = [1,2,3,4,5,]
#
# for i in list22:
#     print(i)

list1 = ['【设计+重构+开发】华为423世界读书日4.20-4.26充值抽奖', '【设计+重构+开发】0501-0505五一男频热门书单', '【设计+重构+开发】4.24-4.26 423世界读书日白牌消费抽奖', '【设计+重构+开发】4.20-4.23 423世界读书日OPPO+VIVO充值翻牌', '【设计+重构+开发】5.1-5.5白牌五一劳动节活动', '【设计+重构+开发】白牌4.20-4.26世界读书日书单', '【设计+重构+开发】白牌消费抽奖5.1-5.3', '【设计+重构+开发】白牌4.20-4.26 423全场免费活动', '【设计+重构+开发】白牌423读书日-销售TOP书籍', '【设计+重构+开发】4.27-4.30OPPO充值排行榜', '【设计+重构+开发】白牌423读书日-充值全额返']
for i in list1:
    if '充值抽奖' in i:
        print('是一个充值抽奖')
    else:
        print('不是一个充值抽奖')


'//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[2]/div/div/div'
'//*[@id="test_plan_content"]/tbody[1]/tr[2]/td[2]/div/div/div'

'//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[3]/div/div[1]/a[2]'
'//*[@id="test_plan_content"]/tbody[1]/tr[2]/td[3]/div/div[1]/a[2]'

'//*[@id="test_plan_content"]/tbody[1]/tr[1]/td[2]/div/div/div/a/i'
'//*[@id="test_plan_content"]/tbody[1]/tr[2]/td[2]/div/div/div/a/i'

'//*[@id="test_plan_content"]/tbody[1]/tr[6]/td[3]/div/div[1]/a[2]'
'//*[@id="test_plan_content"]/tbody[1]/tr[6]/td[3]/div/div[1]/a[2]'