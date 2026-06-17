arr = [1,2,3,4,5,6]
print(arr)
print("left index of three is", arr[:3])
print("right index of three is", arr[3:])
print("balance check")
for i in range(len (arr)):
    l = sum(arr[:i])
    r = sum(arr[:i+1])
    print("index",i,"left sum",l,"right sum",r)
    for i in range(len (arr)):
        if sum(arr[:i]) == sum(arr[i+1:]):
            print("balance point is", i)
