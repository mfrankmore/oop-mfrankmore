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
    print(f"Package Information: \n\t{pkg.dimensions(pkg.containerType)}\n\tWeight: {pkg.weight}\n\tContents: {pkg.contents}\n\tPrice: ${calcCost(pkg)}\n\n")

def calcCost(pkg) -> float:
    containerCharge : float = 0.0
    price : float = 0.0
    pricePerLb : float = 1.5
    
    if pkg.containerType == "Small Box":
        containerCharge = 2.5
    elif pkg.containerType == "Medium Box":
        containerCharge = 5.0
    elif pkg.containerType == "Large Box":
        containerCharge = 7.5
    else:
        raise ValueError(f"Container is of the wrong type: {pkg.containerType}")

    price = (pkg.weight * pricePerLb) + containerCharge

    return price

#Test making packages and running the decorated function
testOrder = Package(12, "GPU", "Medium Box")
makePackage(testOrder)
testOrder2 = Package(11, "Ice Cream", "Small Box")
makePackage(testOrder2)
testOrder3 = Package(4, "Motherboard", "Large Box")
makePackage(testOrder3)