# Tic Tac Toe

# Create the game board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

# Function to check for a win
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[position] == player for position in condition):
            return True
    return False

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()
        print(f"It's Player {current_player}'s turn.")

        move = input('Enter your move (0-8): ')

        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == ' ':
            move = int(move)
            board[move] = current_player

            if check_win(current_player):
                print_board()
                print(f'Player {current_player} wins!')
                game_over = True
            elif ' ' not in board:
                print_board()
                print("It's a tie!")
                game_over = True
            else:
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print('Invalid move. Try again.')

# Play the game
play_game()