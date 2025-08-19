class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
parrot1 = parrot("Polly", 3)
print("Parrot's name is:", parrot1.name)
print("Parrot's age is:", parrot1.age, "years")
print("Parrot's species is:", parrot1.species)