ammount=int(input("Enter the amount: "))
note1 = ammount // 100
note2 = (ammount % 100) // 50
note3 = (ammount % 50) // 20
note4 = (ammount % 20) // 10
note5 = (ammount % 10) // 5
note6 = ammount %   5
print(f"100 notes: {note1}")
print(f"50 notes: {note2}")
print(f"20 notes: {note3}")
print(f"10 notes: {note4}")  
print(f"5 notes: {note5}")
print(f"1 notes: {note6}")