def hotelcost(nights):
    return 140*nights
def planeridecost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        return 0
def rentalcarcost(days):
    cost = 40*days
def tripcosts(city, days, nights):
    return hotelcost(nights) + planeridecosr(city) + rentalcarcost(days)
print("Total currentall costs:", rentalcarcost(5))
print("Total trip costs:", tripcosts("Los Angeles", 5, 2))