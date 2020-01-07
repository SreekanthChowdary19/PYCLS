import unittest # framework 

from calc import *


class TestClass(unittest.TestCase):


    def testValid1(self):
        actual_output = add(10, 20)
        expected_output = 30
        self.assertEqual(expected_output, actual_output, "Test-1 is failed ")

    def testValid2(self):
        actual_output = add(0, 20)
        expected_output = 20
        self.assertEqual(expected_output, actual_output, "Test-2 is failed ")

    def testValid3(self):
        actual_output = sub(100, 20)
        expected_output = 80
        self.assertEqual(expected_output, actual_output, "Test-3 is failed ")

unittest.main()






    
