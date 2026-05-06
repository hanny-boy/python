def Hanoi(n,a,b,c):
    if n == 1:
        print("move disk one from rod ",a,"to rod ",b)
        return
    Hanoi(n-1,a,c,b)
    print("move disk ",n," from rod ",a," to rod",b)
    Hanoi(n-1,c,b,a)
n = 4
Hanoi(n,'a','c','b')