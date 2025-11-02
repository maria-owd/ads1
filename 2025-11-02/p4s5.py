# What does the following algorithm return? What is it’s complexity order?
n = int(input("Enter a positive integer n: "))
i = n // 2 
nr = 0

while i <= n:
    j = n
    while j >= 1:
        nr = nr + 1
        j = j / 2
    i = i + 1
print(nr)

# The algorithm counts the number of times the inner loop executes as 'i' goes from n/2 to n.
# The outer loop runs from n/2 to n, which is approximately n/2 iterations
# The inner loop starts at n and divides j by 2 until j is less than 1, which takes O(log n) time.
# Therefore, the total number of iterations is (n/2) * O(log n)
# Thus, the time complexity of the algorithm is O(n log n).
# The algorithm returns the total count of iterations performed by the inner loop, which is stored in 'nr'.