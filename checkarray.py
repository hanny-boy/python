def checkSorted(a):
    length = len(a)
    if length == 1 or length == 0:
        return True
    return a[0] <= a[1] and checkSorted(a[1:])
a =[1,2,3,4,5,6,7,8,9,10]
if checkSorted(a):
    print("array is sorted")
else:
    print("array is not sorted")