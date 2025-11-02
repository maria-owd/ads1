# which is the best/ worst case of the following algorithm?
n = int(input("Value to be exponentiated: "))
k = int(input("Exponent value: "))
p = 1

while k > 0:
    if k % 2 == 1:
        p = p * n
        k = k - 1
    else:
        n = n * n
        k = k // 2
print(p)

# The algorithm computes n raised to the power of k.
# The best case occurs when k is a power of 2, as it minimizes the number of multiplications needed.
# The worst case occurs when k is odd, as it requires an additional multiplication for each odd k value.
# Therefore, the best case is when k is a power of 2, and the worst case is when k is odd.
# Time complexity for both cases is O(log k), but the number of multiplications differs.