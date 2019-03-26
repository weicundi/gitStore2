import unittest
import testadd
import testsub
from HTMLTestReportCN import HTMLTestRunner
import time

suite = unittest.TestSuite()

suite.addTest(testadd.TestAdd('test_add'))
suite.addTest(testadd.TestAdd('test_add2'))

suite.addTest(testsub.TestSub('test_sub'))
suite.addTest(testsub.TestSub('test_sub2'))

if __name__ == '__main__':

    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename ='./' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：', tester='张三')
    #runner = unittest.TextTestRunner()
    runner.run(suite)
    fp.close()