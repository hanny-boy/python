row = int(input("Enter number of rows: "))
if row % 2 == 0:
    half = row // 2
else:
    half = row // 2 + 1
space = half - 1
for i in range(1, half + 1):
    for j in range(space):
        print(" ", end="")
    space -= 1
    for j in range(1, i + 1):
        print("* ", end="")
    print()