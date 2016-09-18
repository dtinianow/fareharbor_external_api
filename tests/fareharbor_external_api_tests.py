import unittest

def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
# Here's our "unit tests".

# def main():
#     unittest.main()
#
# if __name__ == '__main__':
#     main()

suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
unittest.TextTestRunner(verbosity=2).run(suite)

# def test_success():
#     assert True

# from nose.tools import *
# import fareharbor_external_api
#
# def setup():
#     print "SETUP!"
#
# def teardown():
#     print "TEAR DOWN!"
#
# def test_basic():
#     print "I RAN!"
