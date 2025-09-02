s = input("Enter a string: ")
print(s)
a = len(s)
for i in range(a,0,-1):
    print(s[i-1],end="")