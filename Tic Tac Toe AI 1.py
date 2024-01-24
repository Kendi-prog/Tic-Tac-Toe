import random

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

# Function to make the AI's move
def make_ai_move():
    # Check if AI can win in the next move
    for move in range(9):
        if board[move] == ' ':
            board[move] = 'O'
            if check_win('O'):
                return
            else:
                board[move] = ' '

    # Check if the player can win in the next move and block them
    for move in range(9):
        if board[move] == ' ':
            board[move] = 'X'
            if check_win('X'):
                board[move] = 'O'
                return
            else:
                board[move] = ' '

    # Make a random move
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            board[move] = 'O'
            return

# Function to play the game
def play_game():
    current_player = 'X'
    game_over = False

    while not game_over:
        print_board()

        if current_player == 'X':
            move = input('Enter your move (0-8): ')
            if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == ' ':
                move = int(move)
                board[move] = current_player
            else:
                print('Invalid move. Try again.')
                continue
        else:
            print("AI's turn...")
            make_ai_move()

        if check_win(current_player):
            print_board()
            if current_player == 'X':
                print('You win!')
            else:
                print('AI wins!')
            game_over = True
        elif ' ' not in board:
            print_board()
            print("It's a tie!")
            game_over = True
        else:
            current_player = 'O' if current_player == 'X' else 'X'

# Play the game
play_game()