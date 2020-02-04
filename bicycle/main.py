from wheel import Wheel

print(f"burst pressure = {Wheel.BURST_PRESSURE}")

wheel = Wheel(diameter = 13.0, pressure = 24.0)

print(f"pressure = {wheel.pressure}") # getter for a property
wheel.pressure = 10000.0 # setter notation
print(f"pressure = {wheel.pressure}") # getter for a property
print(f"burst = {wheel.burst}") # getter for a propertyy