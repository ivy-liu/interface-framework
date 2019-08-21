

import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.run_testcase import RunTestCase

testcase_file='testcase_study.xlsx'#用例地址
test=RunTestCase()
test.run(testcase_file)
# ${checkstatus}=[checkstatus]

'''
#1、一次全部运行 unittest.main()
#2、TestSuite 测试套件：可自由组合测试 case，常用的方法是 addTest
suite=unittest.TestSuite()
suite.addTest(MyTest('test_m1'))
suite.addTest(MyTest('test_m2'))
# suite.addTest(MyTest('test_m3'))
runner=unittest.TextTestRunner(verbosity=2)
runner.run(suite)

#3、通过添加类名来运行
# all_suite=unittest.makeSuite(MyTest)#添加类名
# runner=unittest.TextTestRunner(verbosity=2)
# runner.run(all_suite)

'''
