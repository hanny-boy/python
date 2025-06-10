height = int(input("Enter your height in cm:"))
weight = float(input("Enter your weight in kg:"))
hmeter = height / 100
bmi = weight / (hmeter ** 2)
print(f"Your BMI is: {bmi:.2f}")
if bmi < 18.5:
    print("You are underweight.")
elif bmi <= 24.9:
    print("You are healthy.")
elif bmi <= 29.9:
    print("You are overweight.")
else:
    print("You are obese")