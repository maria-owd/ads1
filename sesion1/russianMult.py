'''
Russian Multiplication: 
Consider the following method of multiplication (called ”Russian multiplication”) 
for two nonzero natural numbers, x and y: ”Write x next to y (on the same line). 
Divide x by 2, and write the quotient below x (ignore the remainder for now). 
Multiply y by 2, and write the product below y. 
Continue this process, constructing two columns of numbers. 
Calculations stop when the value 1 is obtained in the first column. 
Add all the values in the second column that correspond to odd values in the first column.

Example: Let x = 13 and y = 25. 

The sequence of results obtained by applying the above operations is as follows:

x   y   remainder
13  25      1           
6   50      0           
3   100     1           
1   200     1           
    325
'''

x = 13
y = 25

r = 0
while x >= 1:
    if x % 2 == 1:
        r += y
    x = x // 2
    y = y * 2

print(r)   

