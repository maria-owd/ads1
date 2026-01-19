'''
- Given two strings, transform one into the other
- Allowed operations: insert, delete, replace
- Break the problem into prefixes of the strings
- Use a DP table where dp[i][j] is the minimum edits for prefixes
- Build the solution from smaller subproblems
- In the end, it should give the minimum number of edits
    needed to transform one string into the other.

'''


def edit_distance(a, b):
    n = len(a)
    m = len(b)

    # dp[i][j] = edit distance between a[0..i-1] and b[0..j-1]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # base cases
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # fill DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete
                    dp[i][j - 1],      # insert
                    dp[i - 1][j - 1]   # replace
                )

    return dp[n][m]

# Example
print(edit_distance("kitten", "sitting"))
