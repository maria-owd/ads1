'''
Directly follows the problem definition and 
    explores all possibilities 
    or performs all required steps explicitly.
'''
def factorial(n):
    result = 1

    for i in range (1, n+1):
        result *= i
    
    return result

n = 4
print("n! = {}".format(factorial(n))) 

'''
- correctness: n!
- time complexity: Θ(n)
- space complexity: Θ(1)
'''