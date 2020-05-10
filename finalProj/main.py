from package import Package
import datetime as DT

#Decorator Function
def shipInfo(orig_func):

    def wrapper(*args, **kwargs):
        print(f"Order Created: {DT.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}")
        return orig_func(*args, **kwargs)

    return wrapper

#Outputs details of the package being created
@shipInfo
def makePackage(pkg):
    print(f"Package Information: \n\t{pkg.dimensions(pkg.containerType)} \n\tWeight: {pkg.weight}\n\tContents: {pkg.contents}\n\n")

testOrder = Package(12, "GPU", "Medium Box")
makePackage(testOrder)
testOrder2 = Package(11, "Ice Cream", "Small Box")
makePackage(testOrder2)
testOrder3 = Package(4, "Motherboard", "Large Box")
makePackage(testOrder3)