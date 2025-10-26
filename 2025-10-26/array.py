# Consider an array x[1..n − 1] 
# containing distinct values from the set $1, 2, . . . , n. 
# Propose a linear complexity algorithm 
# to identify the value from {1, 2, . . . , n} that is not present in the array x.
# Note. Try to solve the problem using auxiliary memory space of size O(1) 
# (this means not using auxiliary vectors).

n = int(input("Number of elements: ")) 
s = 0

for i in range(0, n - 1):
    x = int(input("x[{:d}]: ".format(i + 1)))         
    s = s + x      # the sum of existing elements 

# The sum of all possible values is n * (n+1) // 2
# The missing element is the difference between:
#  the sum of all possible values and 
#  the sum of the existing elements in the array 

m = n * (n + 1) // 2 - s
print(m)

# input: n (no. of elements)
# output: m (the missing element)
# time complexity: O(n) -> 1 for
# space complexity: O(1) -> 1 variable (n)
