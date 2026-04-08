def arrayTotalsum(a):
    length = len(a)
    if length == 1:
        return a[0]
    return a[0]+arrayTotalsum(a[1:])
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,41]
print("array total sum", arrayTotalsum(arr))