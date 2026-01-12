'''
Propose a method based on addition, subtraction, and comparison
operations for determining the integer part of a real number. The integer part (sometimes
called the floor and denoted for a real number x as ⌊x⌋) of a real number is defined as the
largest integer that is less than or equal to the given real number. For example, the integer
part of 2.4 is 2, and for -2.4, it is -3.
'''

f = 2.4
i = 0


if f > 0:
    while i < f-1:
        i += 1
else:
    while i > f:
        i -= 1

print(i) 