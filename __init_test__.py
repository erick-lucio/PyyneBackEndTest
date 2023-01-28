
import unittest


if __name__ == '__main__':
    # unittest.main()
    # discover all tests in the 'tests' directory that match the pattern 'test_*.py'
    tests = unittest.defaultTestLoader.discover('pyyne/challenge/tests', pattern='test_*.py')
    # run the discovered tests
    unittest.TextTestRunner().run(tests)