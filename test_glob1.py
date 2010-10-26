import os
import unittest

class Test(unittest.TestCase):
    def test_glob1s(self):
        from glob import glob1
        
        self.assertEqual(glob1(os.path.dirname(__file__), "test_*.py"),
                         [os.path.basename(__file__)])

if __name__=="__main__":
    unittest.main()

