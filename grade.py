n1 = int(input("Enter a number:"))
n2 = int(input("Enter another number:"))
n3 = int(input("Enter 3rd number:"))
n4 = int(input("Enter 4th number:"))
avg = ( n1 + n2 + n3 + n4) / 4
if avg > 90:
    print("You scored an A! Excellent work!")
elif avg > 80:
    print("You scored a B! Well done!")
elif avg > 70:
    print("You scored a C! Almost there!")
elif avg > 60:
    print("You scored a D! Please work on this subject!")
elif avg > 50:
    print("You scored an E! You need to improve a lot!")
else:
    print("You scored an F! You need to retake the exam!")