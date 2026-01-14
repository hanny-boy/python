n = int(input("Enter a number :"))
originalnumber = n
reversednumber = 0
while n > 0:
    digit = n % 10
    reversednumber = reversednumber * 10 + digit
    n = n//10
if  originalnumber == reversednumber:
    print("It is palindrome.")
else:
    print("It is NOT palindrome")