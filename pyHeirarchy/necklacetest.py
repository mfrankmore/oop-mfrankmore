import unittest

from necklace import Necklace

class NecklaceTest(unittest.TestCase):

    def testConstructor(self):
        necklace = Necklace()
        self.assertEqual(necklace.metal, "gold")
        self.assertEqual(necklace.gem, "diamond")
        self.assertEqual(necklace.polished, True)

    def testNecklace(self):
        testMetal : str = "platinum"
        testGem : str = "ruby"
        necklace = Necklace(metal = testMetal, gem = testGem)
        self.assertEqual(necklace.gem, "ruby")
        self.assertEqual(necklace.metal, "platinum")
        necklace.gem = "pearl"
        necklace.metal = "titanium"
        self.assertEqual(necklace.gem, "pearl")
        self.assertEqual(necklace.metal, "titanium")
        necklace.wear()
        self.assertEqual(necklace.polished, False)
        necklace.polish()
        self.assertEqual(necklace.polished, True)



