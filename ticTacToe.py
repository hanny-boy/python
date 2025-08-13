# Initial empty board
def create_board():
    return {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

def print_board(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    board = create_board()
    boardkeys = list(board.keys())
    player = 'X'
    count = 0

    for i in range(9):
        print_board(board)
        print(f"It's your turn, {player}. Move to which position? (1-9)")
        move = input().strip()

        if move not in boardkeys:
            print("Invalid move! Choose between 1-9.")
            continue

        if board[move] == ' ':
            board[move] = player
            count += 1
        else:
            print("That place is already occupied!")
            continue

        # Check winner after 5 moves
        if count >= 5:
            if (board['7'] == board['8'] == board['9'] != ' ' or
                board['4'] == board['5'] == board['6'] != ' ' or
                board['1'] == board['2'] == board['3'] != ' ' or
                board['7'] == board['4'] == board['1'] != ' ' or
                board['8'] == board['5'] == board['2'] != ' ' or
                board['9'] == board['6'] == board['3'] != ' ' or
                board['7'] == board['5'] == board['3'] != ' ' or
                board['9'] == board['5'] == board['1'] != ' '):
                print_board(board)
                print(f"🎉 Player {player} wins!")
                break

        if count == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Switch player
        player = 'O' if player == 'X' else 'X'

    print("Game Over!")

# Main loop with replay option
while True:
    game()
    replay = input("Do you want to play again? (y/n): ").lower()
    if replay != 'y':
        print("Thanks for playing! 👋")
        break
