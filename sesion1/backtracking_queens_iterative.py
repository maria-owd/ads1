'''
Backtracking is an algorithm design technique that 
    explores all possible solutions step by step.
At each step, the algorithm makes a choice 
    and checks if the partial solution is still valid.
If a partial solution cannot lead to a valid full solution, 
    the algorithm abandons it immediately and goes back to try another choice.

This is an ITERATIVE version using an explicit stack instead of recursion.
'''


"""
Verify if placing a queen at position k (row) with column value col is safe.
Check all previously placed queens (positions 0 to k-1).
"""
def check(board, k, col):
    for i in range(k):
        prev_col = board[i]
        
        # Check if same column
        if prev_col == col:
            return False
        
        # Check if same diagonal
        if abs(i - k) == abs(prev_col - col):
            return False
    
    return True


"""
Iterative backtracking function to place queens.

Uses state variables (k, col) instead of a stack for a more pseudocode-like approach:
- k: current position (0 to n-1)
- col: current column being tried at position k
- When we find a valid placement, we move to next position (k += 1)
- When we exhaust all columns at a position, we backtrack (k -= 1)
"""
def backtrack(k, n, board, solutions):
    # Start at position 0, column 0
    col = 0
    
    while k >= 0:
        # Try to find a valid column for position k
        found = False
        
        for try_col in range(col, n):
            # Check if position is safe
            if check(board, k, try_col):
                # Choice: place queen at position k, column try_col
                board[k] = try_col
                found = True
                col = 0
                k += 1
                break
        
        if not found:
            # No valid column found at position k, must backtrack
            if k < n:
                # Undo: remove queen from position k
                board[k] = -1
            
            # Backtrack to previous position
            k -= 1
            col = board[k] + 1 if k >= 0 else 0
        else:
            # Check if we've placed all queens
            if k == n:
                # Base case: all queens placed successfully
                solutions.append(board.copy())
                # Continue searching for more solutions
                k -= 1
                col = board[k] + 1


"""
Solve N-Queens iteratively using backtracking.
"""
def solve_n_queens(n):
    # Initialize solution array: solution[k] = col where queen is placed at position k
    solution = [-1] * n
    
    # Store all valid solutions
    result = []
    
    # Start iterative backtracking from position 0
    backtrack(0, n, solution, result)
    
    return result


# Drawing function
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

print("N-Queens Problem (Iterative Backtracking)")
print("Number of solutions:", len(sols))
for idx, sol in enumerate(sols, start=1):
    print("\nSolution", idx)
    print(format_solution(sol))
