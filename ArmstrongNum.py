num = int(input("Enter any number:"))
digits = len(str(num))
resultnum = 0
temp = num
while temp > 0:
    digit = temp%10
    resultnum = resultnum + digit**digits
    temp = temp//10
if num == resultnum:
    print("It is an armstong number!")
else:
    print("It is NOT an armstrong number!")