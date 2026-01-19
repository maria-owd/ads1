'''
Divide the problem into independent subproblems of smaller size, 
    solve each recursively, then combine the results.
'''

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return True
        elif x < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

arr = [1, 3, 5, 7, 9, 11]
x = 7

print("is {} in {}? {}".format(x, arr, binary_search(arr, x))) 

'''
- correctness -> invariant: if x exists, it is always in the interval [left, right].
- time complexity. Θ(log n)
- spac complexity: Θ(1)
- remarks: only one subproblem is solved at each step (reduction).
'''