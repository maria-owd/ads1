# consider an array x = [0,..,n]
# return the index of the first strictly postive value encountered (0 not included as positive)
#   traversing from left -> right
# if the value doesn't exist, return -1
# x = [−1, 0, 3,−1, 0, 1]  --> return 2

n = int(input("The number of elements: "))  #problem size: n
x = []
ind = -1

for i in range (0,n):                               
    x.append(int(input("x[{:d}] = ".format(i))))    

    if x[i] > 0:
        if ind == -1:
            ind = i

print(ind)  

# dominant operation: if
# time complexity: Θ(n)
# complexity: O(n)  