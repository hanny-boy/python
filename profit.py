def calcuteprofit(arr,arrsize):
    profit=0
    for i in range(1,arrsize):
        if arr[i]>arr[i-1]:
            profit+=arr[i]-arr[i-1]
    return profit
prices=[700,100,500,300,600,400,8468,394703,798471,3694]
profit=calcuteprofit(prices,len(prices))
print("Maximum profit:",profit)