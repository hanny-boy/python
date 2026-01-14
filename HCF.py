ln = int(input("Enter the largest number : "))
sn = int(input("Enter the smallest number : "))
while sn > 0:
    numberstore = sn
    sn = ln % sn 
    ln = numberstore
print("HCF is ",ln)