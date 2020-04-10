import unittest

from jewelry import Jewelry
from necklace import Necklace
from ring import Ring

class JewelryTest(unittest.TestCase):

    def testRing(self):
        ring = Ring()
        self.assertEqual(ring.polished, True)
        ring.wear()
        self.assertEqual(ring.polished, False)
        ring.polish()
        self.assertEqual(ring.polished, True)

    def testNecklace(self):
        necklace = Necklace()
        self.assertEqual(necklace.polished, True)
        necklace.wear()
        self.assertEqual(necklace.polished, False)
        necklace.polish()
        self.assertEqual(necklace.polished, True)

if __name__ == '__main__':
    unittest.main()
