n = int(input("Enter a number: "))
for i in range(n):
    if n % 5 == 0:
         print("Hanniel")
         pass
    elif n % 3 == 0:
        print("buzz")
    elif n % 2 == 0:
        print("fizz")
    else:
        print(n)