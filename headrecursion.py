def headrecursion(n,num):
    if n > num:
        return
    headrecursion(n+1,num)
    print(n)
n = int(input("Enter n to print 1 to n : "))
headrecursion(1,n)