'''
- Given two strings, find the longest contiguous part common to both
- Use a DP table where dp[i][j] stores the length of the match ending at those positions
- If characters match → extend the substring
- If they don't → reset to 0
- The answer is the maximum value in the table
'''


def longest_common_substring(a, b):
    n = len(a)
    m = len(b)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    max_len = 0
    end_pos = 0  # end position in string a

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i
            else:
                dp[i][j] = 0

    return a[end_pos - max_len:end_pos]

# Example
print(longest_common_substring("ABABC", "BABCA"))
