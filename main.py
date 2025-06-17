units = int(input("Enter the number of units consumed:20"))
if units <= 50 :
    bill = units * 2.60
elif units <= 100 :
    bill = (50 * 2.60) + ((units - 50)) * 3.25
elif units <= 250 :
    bill = (50 * 2.60) + (50 * 3.25) + ((units - 100) * 4.00)
elif units <= 500 :
    bill = (50 * 2.60) + (50 * 3.25) + (150 * 4.00) + ((units - 250) * 4.75)
else:
    bill = (50 * 2.60) + (50 * 3.25) + (150 * 4.00) + (250 * 4.75) + ((units - 500) * 5.20)
print(f"Your total bill is: {bill:.2f} Rs")