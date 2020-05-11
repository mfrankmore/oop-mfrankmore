import unittest

from package import Package

class PackageTest(unittest.TestCase):

    def testConstructor(self):
        package = Package()
        self.assertEqual(package.weight, 0.0)
        self.assertEqual(package.contents, "Empty")
        self.assertEqual(package.containerType, "Medium Box")

    def testPackage(self):
        pkg = Package(10, "Test", "Small Box")
        self.assertEqual(pkg.weight, 10)
        self.assertEqual(pkg.contents, "Test")
        self.assertEqual(pkg.containerType, "Small Box")
        pkg.weight = 15
        self.assertEqual(pkg.weight, 15)
        pkg.contents = "Motherboard"
        self.assertEqual(pkg.contents, "Motherboard")
        pkg.containerType = "Large Box"
        self.assertEqual(pkg.containerType, "Large Box")


