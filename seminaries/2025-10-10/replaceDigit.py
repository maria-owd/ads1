# Propose an algorithm that replaces 
# the appearances of a digit, 
# a in a number with another digit, b. 
# Example n = 1357321, a = 3, b = 9, the number becomes n = 1957921.

n = int(input("Enter an integer: "))
a = int(input("Enter the digit to be replaced (a): "))
b = int(input("Enter the digit to replace with (b): "))

x = 0   # new number
p = 1   # position multiplier
while n != 0:
    digit = n % 10 # extract the last digit
    if digit == a:  # check if it is the digit to replace
        digit = b   # replace it with b
    x = x + digit * p   # add the digit to the new number
    n = n // 10 # remove the last digit from n
    p = p * 10  # update the position multiplier

print("The new number is: ", x)     

