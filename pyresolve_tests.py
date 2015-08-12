from pyresolve import Header
import unittest
import random

class ResolveTests(unittest.TestCase):

    def testheaderlength(self):
        header = Header(random.choice(range(65535)))
        self.assertEqual(len(header.header), 12)

    def testheaderzeros(self):
        "check entries which should be 0"
        header = Header(random.choice(range(65535)))
        headlist = list(map(int, header.header))
        self.assertEqual(headlist[3], 0)
        self.assertEqual(headlist[8], 0)
        self.assertEqual(headlist[9], 0)
        self.assertEqual(headlist[10], 0)
        self.assertEqual(headlist[11], 0)

    def testbadqnum(self):
        "number out of valid range"
        self.assertRaises(ValueError, Header, -1)
        self.assertRaises(ValueError, Header, 65535)
        self.assertRaises(ValueError, Header, -65535)
        self.assertRaises(ValueError, Header, 1.0)


if __name__ == '__main__':
    unittest.main()
