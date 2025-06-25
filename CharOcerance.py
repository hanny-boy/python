s = input("Enter a string:")
char = input("Enter a character to count:")
count = 0
i = 0
while i < len(s):
    if s[i] == char:
        count = count + 1
    i = i + 1
print(f"The character '{char}' appears {count} times in the string '{s}'.")