'''
Solve a problem by calling the same algorithm 
    on smaller inputs until a base case is reached.
'''

def fibonacci(n):
    if n <= 2:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6

print("the {}-th fibonacci nr is {}".format(n, fibonacci(n))) 

'''
- Correctness: correct by induction on n.
- Time complexity: Θ(φ^n)
- Remarks: illustrates inefficiency without memoization.
'''