s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
s2 = {'b', 'a', 'c'}
s3 = list(zip(s1, s2))
print("Zipped sets s1 and s2:", s3)
l1 = [100, 200, 300, 400, 500]
l2 = 10, 20, 30, 40, 50
for x, y in zip(l1, l2[: : - 1]):
    print(x, y)