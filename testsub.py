from calculator import Count
import unittest

class TestSub(unittest.TestCase):

    def setUp(self):
        print('test start')

    def tearDown(self):
        print('test end')

    def test_sub(self):
        '''减法测试1'''
        j = Count(2, 3)
        self.assertEqual(j.sub(), -1)

    def test_sub2(self):
        '''减法测试2'''
        j = Count(76, 41)
        self.assertEqual(j.sub(), 35)

# if __name__ == '__main__':
#     unittest.main()