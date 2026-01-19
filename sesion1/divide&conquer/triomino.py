'''
- The board size is 2ⁿ * 2ⁿ with one missing square

- Goal: cover the rest using L-shaped triominoes (3 squares each)

- Divide & Conquer approach:
    - Split the board into 4 equal quadrants
    - One quadrant already has the missing square

- Key trick:
    - Place one triomino at the center to create a “missing square” in the other 3 quadrants
    - Now each quadrant has exactly one missing square
    - Recursively solve the same problem for each smaller quadrant

Base case:
    A 2 * 2 board → place exactly one triomino

Conclusion:
    Reduce the problem to four smaller boards 
        by placing one central triomino so each subproblem looks the same.
'''


tile_id = 1

def triomino(board, size, top, left, missing_r, missing_c):
    global tile_id

    if size == 2:
        # Base case: 2x2 board
        for i in range(2):
            for j in range(2):
                r = top + i
                c = left + j
                if r != missing_r or c != missing_c:
                    board[r][c] = tile_id
        tile_id += 1
        return

    half = size // 2
    current_tile = tile_id
    tile_id += 1

    # Center positions
    centers = [
        (top + half - 1, left + half - 1),  # top-left
        (top + half - 1, left + half),      # top-right
        (top + half, left + half - 1),      # bottom-left
        (top + half, left + half)           # bottom-right
    ]

    # Determine which quadrant has the missing square
    quad = 0
    if missing_r < top + half and missing_c < left + half:
        quad = 0
    elif missing_r < top + half and missing_c >= left + half:
        quad = 1
    elif missing_r >= top + half and missing_c < left + half:
        quad = 2
    else:
        quad = 3

    # Place center triomino
    for i in range(4):
        if i != quad:
            r, c = centers[i]
            board[r][c] = current_tile

    # Recurse into 4 quadrants
    triomino(board, half, top, left,
             missing_r if quad == 0 else centers[0][0],
             missing_c if quad == 0 else centers[0][1])

    triomino(board, half, top, left + half,
             missing_r if quad == 1 else centers[1][0],
             missing_c if quad == 1 else centers[1][1])

    triomino(board, half, top + half, left,
             missing_r if quad == 2 else centers[2][0],
             missing_c if quad == 2 else centers[2][1])

    triomino(board, half, top + half, left + half,
             missing_r if quad == 3 else centers[3][0],
             missing_c if quad == 3 else centers[3][1])


# Example

n = 3                  # board size = 2^n
size = 2 ** n
board = [[0]*size for _ in range(size)]

missing_r, missing_c = 1, 2
board[missing_r][missing_c] = -1  # mark missing square

triomino(board, size, 0, 0, missing_r, missing_c)

for row in board:
    print(row)
