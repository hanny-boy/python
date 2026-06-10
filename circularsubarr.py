def kande(arr):
    arrsize = len(arr)
    max = 0
    cmax = 0
    for i in range(0,arrsize):
        cmax = cmax + arr[i]
        if(cmax < 0):
            cmax = 0
        if(max < cmax):
            max = cmax
    return max
def circularsum(arr):
    arrsize = len(arr)
    max_kande = kande(arr)
    maxwrap = 0
    for i in range(0, arrsize):
        maxwrap = maxwrap + arr[i]
        arr[i] = -arr[i]
    maxwrap = maxwrap + kande(arr)
    if(maxwrap > max_kande):
        return maxwrap
    else:
        return max_kande
a = [1,2,3,5,6,9,11,12,13,15,16,19,21,22,23,25,26,29]
print("Maximum circular subarray is", circularsum(a))