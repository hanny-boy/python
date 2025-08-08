import array as arr
num = arr.array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print("Original array is", num)
c = num.count(1)
print("Number of occurrences of 1 are", c)
num.reverse()
print("Reversed array is", num)