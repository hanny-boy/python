def tree(n,num):
    if (n < 1 , n > num):
        return
    print(n)
    tree(n-1,num)
    print(n)
n = int(input("Enter any number : "))
tree(n,n)