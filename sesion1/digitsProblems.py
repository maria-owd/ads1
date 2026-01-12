'''
(Operations with natural numbers and digits) Let n be a nonzero natural number. Describe
in pseudocode the algorithms for:
(a) Finding the sum of all digits of n. For example, for n= 26326, the value is 19.
(b) Finding the value obtained by reversing the digits of n. For example, for the value
n= 26326, the value is 62362.
(c) Finding the set of all digits that occur in the number. For example, for the value n =
26326, is formed from the set {2,3,6}of digits.
(d) Count how many values of 1 are in the binary representation of n'''

# (a) Finding the sum of all digits of n. For example, for n= 26326, the value is 19.
def sumDigits(n: int):
    s = 0
    while n > 0:
        d = n % 10
        s += d
        n = n // 10
    return s

#(b) Finding the value obtained by reversing the digits of n. 
# For example, for the value n= 26326, the value is 62362.
def reverseDigits(n: int):
    x = 0
    while n > 0:
        d = n % 10
        x = x * 10 + d
        n //= 10
    return x

# c)
def setDigi(n: int):
    l = set()
    while n > 0:
        d = n % 10
        l.add(d)
        n = n // 10
    return l

# d)
def binaryVal(n: int):
    binval = "{:b}".format(n)
    print(binval) 

    c = 0
    while n > 0:
        r = n % 2
        c += r 
        n //= 2
    return c 
    
    
n = 26326


print("sum digits:", sumDigits(n))
print("reverse digits:", reverseDigits(n))
print("the set of digits: ", setDigi(n)) 
print("1 binary appear: ", binaryVal(n)) 