from package import Package
import datetime as DT

#Decorator Function
def ship(orig_func):

    def wrapper(*args, **kwargs):
        print(f"Order Created: {DT.datetime.now().strftime('%Y-%m-%d-%H')}")
        return orig_func(*args, **kwargs)

    return wrapper

#Outputs details of the package being created
def makePackage(pkg):
    print(f"Package Information: \n\t {pkg.dimensions()} \n\tContents: {pkg.contents}\n\n"



