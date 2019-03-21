from calculator import Count
import unittest

class MyTest(unittest.TestCase):

    def setUp(self):
        print('test start')

    def tearDown(self):
        print('test end')

class TestCount(unittest.TestCase):

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5)

    def test_add2(self):
        j = Count(41, 76)
        self.assertEqual(j.add(), 117)

    def test_case(self):
        self.assertTrue(Count.is_prime(7),msg='Is not prime' )



if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(TestCount('test_case'))
    runner = unittest.TextTestRunner()
    runner.run(suite)

