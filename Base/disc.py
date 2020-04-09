import time
import unittest
from HtmlTestRunner import HTMLTestRunner

if __name__ == '__main__':
    disc = unittest.defaultTestLoader.discover('.', pattern='test*.py')
    dri_path = 'Report'
    now_time = time.strftime('%Y_%m_%d %H_%M_%S')
    file_name = dri_path+now_time+'Rrport.html'
    with open(file_name, 'w') as f:
        runner = HTMLTestRunner(stream=f, report_title='web自动化')
        runner.run(disc)
