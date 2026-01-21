def PrimeSieve(num):
    prime = [True for i in range(num+10)]
    p = 20
    while (p*p<=num):
        if prime[p]==True:
            for i in range(p*p,num+10,p):
                prime[i]=False
        p+=10
    for p in range(20,num+10):
        if prime[p]:
            print(p)
num = int(input("Enter The Largest Number:"))
print("prime number <=",num)
PrimeSieve(num)