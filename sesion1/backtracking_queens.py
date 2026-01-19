'''
Backtracking is an algorithm design technique that 
    explores all possible solutions step by step.
At each step, the algorithm makes a choice 
    and checks if the partial solution is still valid.
If a partial solution cannot lead to a valid full solution, 
    the algorithm abandons it immediately and goes back to try another choice.
'''


"""
Verify if placing a queen at (row, col) is safe.
Check all previously placed queens (rows 0 to row-1).
"""
def check_partial_option(board, row, col):

    for prev_row in range(row):
        prev_col = board[prev_row]
        
        # Check if same column
        if prev_col == col:
            return False
        
        # Check if same diagonal (difference of rows equals difference of columns)
        if abs(prev_row - row) == abs(prev_col - col):
            return False
    
    return True


"""
Recursive backtracking function to place queens.
"""
def backtrack(row, n, board, solutions):
    # Base case: all queens placed successfully
    if row == n:
        solutions.append(board.copy())
        return
    
    # Recursive case: try placing a queen in each column of current row
    for col in range(n):
        # Check if position is safe
        if check_partial_option(board, row, col):
            # Choice: place queen
            board[row] = col
            
            # Explore: go to next row
            backtrack(row + 1, n, board, solutions)
            
            # Undo: remove queen and backtrack
            board[row] = -1


"""
Recursive backtracking function to place queens.
"""
def solve_n_queens(n):
    # Initialize solution array: solution[k] = col where queen is placed at position k
    solution = [-1] * n
    
    # Store all valid solutions
    result = []
    
    # Start backtracking from position 0
    backtrack(0, n, solution, result)
    
    return result



# drawing
def format_solution(solution):
    n = len(solution)
    lines = []
    for r in range(n):
        row = []
        for c in range(n):
            row.append("Q" if solution[r] == c else ".")
        lines.append(" ".join(row))
    return "\n".join(lines)



n = 4
sols = solve_n_queens(n)

print("Number of solutions:", len(sols))
for idx, sol in enumerate(sols, start=1):
    print("\nSolution", idx)
    print(format_solution(sol))
