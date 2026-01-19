'''
Reduce the problem to a smaller instance of the same problem,
    solve it, then extend the solution. (also known as reduction technique)
'''

def power(x, n):
    if n == 0:
        return 1
    
    p = power(x, n//2)

    if n % 2 == 0:
        return p * p
    else:
        return p * p * x

x = 2
n = 3

print("x^n = {}".format(power(x,n))) 

'''
- correctness: correct by induction on n using the recursive definition of exponentiation
- time complexity: Θ(log n)
- space complexity: Θ(log n)
- remark: Uses recurrence T(n)=T(n/2)+1
'''