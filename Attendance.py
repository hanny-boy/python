Attendance =  int(input("Enter the number of students present: "))
Medical = ("Do you have medical costs? (yes/no): ").lower()
if Attendance >= 75 : 
    print ("You can do the exam.")
else:
    if Medical == "yes":
        print ("You can do the exam.")
    else:
        print ("You can't do the exam.")