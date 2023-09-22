draw_numbers = [1,76,38,96,62,41,27,33,4,2,94,15,89,25,66,14,30,0,71,21,48,44,87,73,60,50,77,45,29,18,5,99,65,16,93,95,37,3,52,32,46,80,98,63,92,24,35,55,12,81,51,17,70,78,61,91,54,8,72,40,74,68,75,67,39,64,10,53,9,31,6,7,47,42,90,20,19,36,22,43,58,28,79,86,57,49,83,84,97,11,85,26,69,23,59,82,88,34,56,13]

def lines_to_matrix(lines):
    matrix = []
    for line in lines:
        row = [int(x) for x in line.strip().split()]
        matrix.append(row)
    return matrix


def print_boards(boards):
    # Print boards
    for i, board in enumerate(boards):
        print(f"Board {i + 1}:")
        for row in board:
            print(row)
        print()

# Read the text file
def read_boards(URL) :
    with open(URL, 'r') as file:
        lines = file.readlines()

    boards = []
    current_board = []

    for line in lines:
        if line.strip():  # Non-empty line
            current_board.append(line)
        elif current_board:  # Empty line and we have data
            board = lines_to_matrix(current_board)
            boards.append(board)
            current_board = []

    # Add the last board if the last line isn't empty
    if current_board:
        matrix = lines_to_matrix(current_board)
        boards.append(matrix)
    
    return boards

def check_win(marked_board):
    # Check rows
    for row in marked_board:
        if all(row):
            return True

    # Check columns
    for i in range(5):
        if all([row[i] for row in marked_board]):
            return True

    return False

def calculate_score(board, marked_board):
    score = 0
    for i, row in enumerate(board):
        for j, number in enumerate(row):
            if not marked_board[i][j]:
                score += number
    return score

############## INITIALIZE BOARDS ##############
boards = read_boards('boards.txt')
marked_boards = [[[False] * len(row) for row in board] for board in boards]
boards_score  = [None] * len(boards)

############## DRAW NUMBERS ##############
for drew_number in draw_numbers:
    # Update boards with drew number
    for i, board in enumerate(boards):
        for j, row in enumerate(board):
            for k, number in enumerate(row):
                if number == drew_number:
                    marked_boards[i][j][k] = True
    
    # Check win condition
    for i in range(len(marked_boards)):
        if not boards_score[i] and check_win(marked_boards[i]):
            boards_score[i] = calculate_score(boards[i], marked_boards[i]) * drew_number
            print(f"Board {i + 1} won with score {boards_score[i]}")
    
    # Stop the game if all boards have won
    if all(score is not None for score in boards_score) :
        print("All boards have won!")
        break
