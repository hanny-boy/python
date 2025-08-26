class Vechile:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vechile):
    pass
sd = Bus("School Drive", 180, 12)
print("Name Of Vechile:", sd.name, "MaxSpeed:", sd.max_speed, "Mileage:", sd.mileage)