'''
Determine the base-10 value of a natural number starting from its binary digit sequence.
Propose a method based only on elementary operations (addition, subtraction, multiplication
- exponentiation is not considered an elementary operation). The goal is to minimize the
number of operations involved.
'''

b = '1011100'
print(b)

b = b[::-1]
p = 1
x = 0
for d in b:
    d = int(d)
    x = x + p * d
    p *= 2

print(x) 

