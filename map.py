n1 = [1, 2, 3, 4, 5]
n2 = [6, 7, 8, 9, 10]
Result = map(lambda x, y: x + y, n1, n2)
print("Result of adding corresponding elements:", list(Result))
n = [1, 2, 3, 4, 5]
def square(x):
    return x * x
r = map(square, n)
print("Result of squaring elements:", list(r))