from calculator import Count
import unittest

class TestAdd(unittest.TestCase):

    def setUp(self):
        print('test start')

    def tearDown(self):
        print('test end')

    def test_add(self):
        '''加法测试1'''
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        '''加法测试2'''
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

# if __name__ == '__main__':
#     unittest.main()