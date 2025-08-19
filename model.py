class vechile:
    def __init__(self, mileage, MaximumSpeed):
        self.mileage = mileage
        self.MaximumSpeed = MaximumSpeed
modelX = vechile(240, 18)
print("model Maximum Speed is:", modelX.MaximumSpeed, "km/h")
print("model mileage is:", modelX.mileage, "km/l")