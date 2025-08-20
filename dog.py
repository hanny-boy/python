class dog:
    species = "Shiba Inu"
    def __init__(self, name, age):
        self.name = name
        self.age = age
dog1 = dog("William", 4)
print("Dog's name is:", dog1.name)
print("Dog's age is:", dog1.age, "years")
print("Dog's species is:", dog1.species)