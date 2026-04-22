def ways(n, memo={}):
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = ways(n - 1, memo) + ways(n - 2, memo)
    return memo[n]


stairs = int(input("Enter number of steps: "))
print("Number of ways to climb stairs is", ways(stairs))