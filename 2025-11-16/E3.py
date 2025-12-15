n = int(input("Matrix size: "))  
A = []

for i in range(0,n):
    row = []
    for j in range(0,n):                
        row.append(int(input("A[{:d}][{:d}] = ".format(i,j))))   
    A.append(row)

allzero = True

for i in range (0, n):
    for j in range (i+1, n):
        if A[i][j] != 0:
            allzero = False 

print(allzero)

# problem size: n^2
# dominant operation: if
# time execution: (n * (n-1)) / 2
# complexity: O(n^2)
