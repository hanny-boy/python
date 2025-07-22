import random
print("I will guess a number between 10 and 20 and you will have to predict it.")
playing = True
number = random.randint(10, 20)
while playing:
    guess = int(input("Enter your guess:"))
    if guess == number:
        print("You win the game! You are a math genius!")
        playing = False
    else:
        print("Your guess isn't quite right. Try again!")