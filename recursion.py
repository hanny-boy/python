def displaynum(n):
    if n > 100:
        return
    print(n)
    displaynum(n+1)
displaynum(1)