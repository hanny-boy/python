try:
    age = int(input("Enter your age: "))
    print("The age entered is", age)
except ValueError as e:
    print("Exception occurred:", e)
    print("Please enter a valid integer for age.")