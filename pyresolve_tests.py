from pyresolve import Header
import unittest
import random

class ResolveTests(unittest.TestCase):

    def testheaderlength(self):
        header = Header(random.choice(range(65535)))
        self.assertEqual(len(header.header), 12)


if __name__ == '__main__':
    unittest.main()
