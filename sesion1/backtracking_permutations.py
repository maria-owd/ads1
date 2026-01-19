"""
Generate all permutations of a set of numbers using backtracking.
A permutation is an arrangement of all elements where order matters.

The backtracking approach:
1. Track which numbers have been used
2. At each position, try each unused number
3. When a complete permutation is formed, add it to results
4. Backtrack by removing the last added number and marking it as unused
"""


"""
Check if a number can be added to the current permutation.
A number is valid if it hasn't been used yet in the current permutation.
"""
def check(num, current_permutation):
    # Check if the number has already been used
    return num not in current_permutation


"""
Recursive backtracking function to generate permutations.
"""
def backtrack(position, n, numbers, current_permutation, all_permutations):
    # Base case: all positions filled
    if position == n:
        # We have a complete permutation
        all_permutations.append(current_permutation.copy())
        return
    
    # Recursive case: try each number at current position
    for num in numbers:
        # Check if this number can be used
        if check(num, current_permutation):
            # Choice: add this number to the current permutation
            current_permutation[position] = num
            
            # Explore: recursively fill the next position
            backtrack(position + 1, n, numbers, current_permutation, all_permutations)
            
            # Undo: remove the number (backtrack)
            current_permutation[position] = None


"""
Generate all permutations of a given set of numbers.
"""
def generate_permutations(numbers):
    n = len(numbers)
    # Initialize solution array
    current_permutation = [None] * n
    
    # Store all valid permutations
    result = []
    
    # Start backtracking from position 0
    backtrack(0, n, numbers, current_permutation, result)
    
    return result


# Test with a set of numbers
numbers = [1, 2, 3]
perms = generate_permutations(numbers)

print(f"Generating all permutations of {numbers}")
print(f"Number of permutations: {len(perms)}")
print("\nAll permutations:")

for idx, perm in enumerate(perms, start=1):
    print(f"{idx}. {perm}")
