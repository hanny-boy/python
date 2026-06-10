def kande_algorithm(arr, arrsize):
    max = -999
    cmax = 0
    for i in range(0, arrsize):
        cmax = cmax + arr[i]
        if(max < cmax):
            max = cmax
        if(cmax < 0):
            cmax = 0
    return max
a = [1,2,3,5,6,9,11,12,13,15,16,19,21,22,23,25,26,29]
print("Maximum subarray is", kande_algorithm(a, len(a)))