"""
Generate all subsets (power set) of a set of numbers using backtracking.
A subset is any combination of elements, where order doesn't matter.

The backtracking approach:
1. For each element, decide whether to include it or not
2. At each position, try including and excluding the element
3. All partial solutions are valid subsets
4. Backtrack by removing the last added element
"""


"""
Check if an element can be added to the current subset.
An element is valid if its index is greater than the last added element's index
to avoid duplicates (e.g., [1,2] and [2,1] are the same subset).
"""
def check(index, start_index):
    # Check if we haven't gone past the starting index
    return index >= start_index


"""
Recursive backtracking function to generate subsets.
"""
def backtrack(start_index, n, numbers, current_subset, all_subsets):
    # Base case: always add the current subset (even if empty)
    all_subsets.append(current_subset.copy())
    
    # Recursive case: try adding each remaining element
    for i in range(start_index, n):
        # Check if this element can be added
        if check(i, start_index):
            # Choice: add this element to the current subset
            current_subset.append(numbers[i])
            
            # Explore: recursively build subsets starting from next element
            backtrack(i + 1, n, numbers, current_subset, all_subsets)
            
            # Undo: remove the element (backtrack)
            current_subset.pop()


"""
Generate all subsets of a given set of numbers.
"""
def generate_subsets(numbers):
    n = len(numbers)
    # Initialize current subset as empty list
    current_subset = []
    
    # Store all valid subsets
    result = []
    
    # Start backtracking from index 0
    backtrack(0, n, numbers, current_subset, result)
    
    return result


# Test with a set of numbers
numbers = [1, 2, 3]
subsets = generate_subsets(numbers)

print(f"Generating all subsets of {numbers}")
print(f"Number of subsets: {len(subsets)} (should be 2^{len(numbers)} = {2**len(numbers)})")
print("\nAll subsets:")

for idx, subset in enumerate(subsets, start=1):
    print(f"{idx}. {subset}")
