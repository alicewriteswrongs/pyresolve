from pyresolve import Header
import unittest
import random

class ResolveTests(unittest.TestCase):

    def testheaderlength(self):
        header = Header(random.choice(range(65535)))
        self.assertEqual(len(header.header), 12)

    def testheaderzeros(self):
        header = Header(random.choice(range(65535)))
        headlist = list(map(int, header.header))
        self.assertEqual(headlist[3], 0)
        self.assertEqual(headlist[8], 0)
        self.assertEqual(headlist[9], 0)
        self.assertEqual(headlist[10], 0)
        self.assertEqual(headlist[11], 0)


if __name__ == '__main__':
    unittest.main()
