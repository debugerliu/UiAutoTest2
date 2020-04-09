import unittest

from Base.buess import BaiDuSearch


class TestS(unittest.TestCase):

    def setUp(self) -> None:
        print('开始了')

    def test(self):
        bs = BaiDuSearch()
        bs.test_search()
