class employee:
    def __init__(self):
        print("Employee Created!")
    def __del__(self):
        print("Employee Deleted!")
def createemployee():
    emp = employee()
    print("Making Object..")
    obj = employee()
    print("Function End..")
obj = createemployee()
print("Program End..")