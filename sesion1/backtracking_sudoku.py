"""
Solve a Sudoku puzzle using backtracking.
Sudoku is a 9x9 grid where each row, column, and 3x3 box must contain digits 1-9.

The backtracking approach:
1. Find an empty cell
2. Try placing digits 1-9 in that cell
3. Check if the placement is valid (row, column, and box constraints)
4. If valid, recursively fill the rest of the board
5. If no valid digit works, backtrack and try a different digit
"""


"""
Check if placing a number at board[row][col] is valid.
A number is valid if it doesn't already exist in:
- The same row
- The same column  
- The same 3x3 box
"""
def check(board, row, col, num):
    # Check if num is already in the row
    for c in range(9):
        if board[row][c] == num:
            return False
    
    # Check if num is already in the column
    for r in range(9):
        if board[r][col] == num:
            return False
    
    # Check if num is already in the 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for r in range(box_row_start, box_row_start + 3):
        for c in range(box_col_start, box_col_start + 3):
            if board[r][c] == num:
                return False
    
    return True


"""
Find the next empty cell in the board (marked with 0).
Returns (row, col) tuple or None if no empty cell exists.
"""
def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None


"""
Recursive backtracking function to solve Sudoku.
"""
def backtrack(board):
    # Base case: find the next empty cell
    empty = find_empty_cell(board)
    
    # If no empty cell, board is complete
    if empty is None:
        return True
    
    row, col = empty
    
    # Recursive case: try placing digits 1-9
    for num in range(1, 10):
        # Check if this number can be placed
        if check(board, row, col, num):
            # Choice: place the number
            board[row][col] = num
            
            # Explore: recursively solve the rest
            if backtrack(board):
                return True
            
            # Undo: remove the number (backtrack)
            board[row][col] = 0
    
    # No valid number found, trigger backtracking
    return False


"""
Solve a Sudoku puzzle.
"""
def solve_sudoku(board):
    # Solve the board in-place
    if backtrack(board):
        return board
    else:
        return None


"""
Print the Sudoku board in a readable format.
"""
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j], end=" ")
        print()


# Test with a sample Sudoku puzzle (0 represents empty cells)
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Original Sudoku puzzle:")
print_board(puzzle)

solution = solve_sudoku(puzzle)

if solution:
    print("\n" + "="*21)
    print("Solved Sudoku:")
    print_board(solution)
else:
    print("\nNo solution exists for this puzzle.")
