import unittest

from ring import Ring

class RingTest(unittest.TestCase):
    
    def testConstructor(self):
        ring = Ring()
        self.assertEqual(ring.metal, "gold")
        self.assertEqual(ring.gem, "none")
        self.assertEqual(ring.size, 6)
        self.assertEqual(ring.polished, True)

    def testNecklace(self):
        testMetal : str = "platinum"
        testGem : str = "ruby"
        testSize : int = 8
        ring = Ring(metal = testMetal, gem = testGem, size = testSize)
        self.assertEqual(ring.gem, "ruby")
        self.assertEqual(ring.metal, "platinum")
        ring.gem = "pearl"
        ring.metal = "titanium"
        ring.size = 7
        self.assertEqual(ring.gem, "pearl")
        self.assertEqual(ring.metal, "titanium")
        ring.wear()
        self.assertEqual(ring.polished, False)
        ring.polish()
        self.assertEqual(ring.polished, True)