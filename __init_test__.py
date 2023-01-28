
import unittest


if __name__ == '__main__':
    tests = unittest.defaultTestLoader.discover('pyyne/challenge/tests', pattern='test_*.py')    
    unittest.TextTestRunner().run(tests)