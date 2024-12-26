
# Main idea here to is design some kind of cipher that can encode one specific position, regardless of initial condition of the board.
# Inputs from clark gave this solution. I just simulate it here

# For each chess board pieces, encode position in binary. This yeirds are 6 bit bindary representation.
# For each chess board position, XOR all position codes that has coin in heads position. Output of the XOR is the position of the key spot.

# For first prisoner, they will have a random output. But output of the algorithm can be manipulated by flipping any one coin.

# Algorithm:
# First prisoner:
# 1. XOR All black pieces
# 2. XOR key position with output of step 1
# 3. Flip coin at position output by step 2


import random

random.seed(1234567)


def solver(board_state, key_position):
    """
    Solver for the clark algorithm

    For each position, if coin is HEAD (1), XOR it's position with buffer
    Finally XOR buffer with key_position

    params:

    board_state:  list of n element, n being board size, containing bools to represent if coin is head or tail
    key_position:  encoded position of key. Int of index of the key.
    
    """
    if key_position >= len(board_state):
        raise RuntimeError("Key Position out of range")
    
    buffer = 0

    for cin in range(len(board_state)):
        if board_state[cin]:
            buffer = buffer ^ cin
    print(f"Existing State XOR: {buffer}")

    solution = (buffer ^ key_position) % len(board_state)

    return solution


def checker(board_state, key_position, solution):
    """
    Checker for solution % len(board)
    """

    if key_position >= len(board_state):
        raise RuntimeError("Key Position out of range")
    
    if solution >= len(board_state):
        raise RuntimeError("Soltion out of range")
    
    # Flip coin
    board_state[solution] = 0 if board_state[solution] else 1

    # Calculate Buffer
    buffer = 0
    for cin in range(len(board_state)):
        if board_state[cin]:
            buffer = buffer ^ cin
    
    print(f"Key Found: {buffer}")
    
    return ( buffer == key_position )
    


if __name__ == "__main__":
    board = [0,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0]
    key = 2


    print(f"Brd: {board}")

    keyboard = []
    for i in range(len(board)):
        if i == key:
            keyboard.append(1)
        else:
            keyboard.append(0)
    print(f"Key: {keyboard}" )

    print(f"Key Position: {key}")

    sol = solver(board, key)
    print(f"Solution: {sol}")

    check = checker(board, key, sol)

    # Check
    if check:
        print ("Solution Good")
    else:
        print("Wrong")