def tailrecursion(n,num):
    if n > num:
        return
    print(n)
    tailrecursion(n+1,num)
n = int(input("Enter the number : "))
tailrecursion(1,n)