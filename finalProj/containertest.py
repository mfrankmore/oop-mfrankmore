import unittest

from container import Container

class ContainerTest(unittest.TestCase):

    def testConstructor(self):
        container = Container()
        self.assertEqual(container.containerType, "Medium Box")

    def testContainer(self):
        container = Container("Small Box")
        container.containerType = "Small Box"
        self.assertEqual(container.containerType, "Small Box")
        container.containerType = "Medium Box"
        self.assertEqual(container.containerType, "Medium Box")
        container.containerType = "Large Box"
        self.assertEqual(container.containerType, "Large Box")
        testString = "Dimensions: 8 x 8 x 4."
        self.assertEqual(container.dimensions(container.containerType), testString)