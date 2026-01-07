def printfactor(number):
    print("THe factors of the number are")
    for i in range(1,number+1):
        if number%i==0:
            print(i)
number = int(input("Write you number"))
printfactor(number)