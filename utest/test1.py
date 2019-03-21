import unittest

class Test(unittest.TestCase):

    def setUp(self):
        number = input('Enter a number')
        self.number = int(number)

    def test_Case(self):
        self.assertEqual(self.number, 10, msg='You input is not 10')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()