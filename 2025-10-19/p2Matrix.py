# matrix with m rows and n columns
from random import random

m = 10
n = 15
matrix = [[int(random() * 100) for _ in range(n)] for _ in range(m)]  #init. with random numbers

# a) display the elements of the matrix row by row
for i in range(m):
    print("row {}: ".format(i), end = '')
    for j in range(n):
        print("{:2d} ".format(matrix[i][j]), end = '')
    print()
print()

# b) display the elements of the matrix column by column
for j in range(n):
    print("col {}: ".format(j), end = '')
    for i in range(m):
        print("{:2d} ".format(matrix[i][j]), end = '')
    print()
print()

# c) display the elements of the diagonal matrix and the parallel lines
maxim = max(m, n)   # create a super sqaure matrix
for j in range(maxim - 1, -maxim, -1):  # parse it in reverse
    for i in range(0, maxim):
        if 0 <= i < m and 0 <= i + j < n:
            print("{:2d} ".format(matrix[i][i + j]), end = '')
    print()

# d) display the elements in a spiral
k = m * n # number of total elements to display
step_i = 0      # step for i
step_j = 1      # step for j
min_i = 0       # minimum for i
max_i = m - 1   # maximum for i
min_j = 0       # minimum for j
max_j = n - 1   # maximum for j
i = 0           # starting position
j = 0           # starting position

while k > 0:    
    # 1: print position
    print("{:2d} ".format(matrix[i][j]), end = '')

    # 2: count another printed position:
    k -= 1

    # 3: move to the next position:
    i = i + step_i
    j = j + step_j

    # 4: check the limits (to see if we're out of the matrix):
    if j > max_j:   #checking the right limit
        # 4.1: move back to the matrix:
        j = max_j
        i += 1
        # 4.2: change the direction:
        step_i = 1 
        step_j = 0
        # 4.3: mark the completed row and change the limit:
        min_i += 1

    if i > max_i:   #checking the bottom limit
        i = max_i
        j -= 1
        step_i = 0
        step_j = -1
        max_j -= 1
    
    if j < min_j:   #checking the left limit
        j = min_j
        i -= 1
        step_i = -1
        step_j = 0
        max_i -= 1 
    
    if i < min_i:   #checking the upper limit
        i = min_i
        j += 1
        step_i = 0
        step_j = 1
        min_j += 1
print()        