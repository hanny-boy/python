def billammount(bill, tipper):
    total = bill * (1 + 0.01 * tipper)
    total = round(total, 2)
    print ("The total bill ammount is", total)
billammount(100, 15)