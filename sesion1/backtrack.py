'''
Explores the solution space incrementally and abandons partial solutions that violate
constraints.
'''

def permutations(arr, pos=0):
    if pos == len(arr):
        print(arr)
        return

    for i in range(pos, len(arr)):
        arr[pos], arr[i] = arr[i], arr[pos]
        permutations(arr, pos + 1)
        arr[pos], arr[i] = arr[i], arr[pos]


arr = [1, 2, 3]
"permutations {}".format(permutations(arr))

'''
- correctness: correct because all valid configurations are explored eactly once
- time complexity: Θ(n!)
- space complexity: Θ(n)
- remarks: worst-case exponential complexity 
'''