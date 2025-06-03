import random

name = input ("Enter your name: ")
age = int (input ("Enter your age: "))

print (f"Hello {name}, welcome to the game!")

print ("Let's start the game!")

done = True
while done:
    if age >= 5 & age < 7:
        n1 = random.randint (1, 9)
        n2 = random.randint (1, 9)
        
        print (f"What is {n1} + {n2}?")
        answer = int (input (f"{n1} + {n2} = "))
        
        if answer == n1 + n2:
            print ("Correct!")
        else:
            print ("Incorrect!")

        continue_game = input ("Do you want to continue? (Y/n): ")

        if continue_game.lower() == 'n':
            done = False
            print ("Thanks for playing!")
            exit()