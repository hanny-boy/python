try:
    num1, num2 = eval(input("Enter 2 numbers separated by commas "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError as e:
    print("Division by 0 is not allowed")
except SyntaxError as se:
    print("Invalid input, please enter two numbers separated by a comma")
except Exception as sea:
    print("Invalid input")
else:
    print("No exception")
finally:
    print("This will execute no matter what")