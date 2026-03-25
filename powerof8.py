def checkpowerof8(n):
    if n < 0:
        return False
    while n%8 == 0:
            n = n//8
    return n == 1
n = int(input("Enter a number: "))
if checkpowerof8(n):
     print(n,"is power of eight.")
else:
     print(n,"is not power of eight.")