import random
print("Lets play a game of paper scissors rock!")
while True:
    user_input = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
    possible_choices = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_choices)
    print(f"You chose {user_input}, computer chose {computer_action}.")
    if user_input == computer_action:
        print("It's a tie!")
    elif (user_input == "rock"):
        if computer_action == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif (user_input == "paper"):
        if computer_action == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif (user_input == "scissors"):
        if computer_action == "paper":
            print("You win!")
        else:
            print("You lose!")
    elif user_input == "exit":
        print("Thanks for playing!")
        break
    else:
        print("Invalid input. Please enter rock, paper, or scissors.")