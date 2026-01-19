'''
Dynamic Programming (DP) is an algorithm design technique used when 
    a problem can be broken into overlapping subproblems and has optimal substructure.
Instead of solving the same subproblem many times, 
    DP stores intermediate results and reuses them.

Core idea:
    - build solutions for small values first
    - store them in a table (array)
    - use those stored values to construct solutions for larger values
'''

'''
Task:
    Given a target sum and a set of coin values, 
        determine the minimum number of coins needed to form the sum.
'''

def min_coins_dp(S, coins):
    big = 10**9              # value larger than any possible solution

    best = [big] * (S + 1)   # best[x] = min coins for sum x
    last = [-1] * (S + 1)    # last[x] = last coin used for x

    best[0] = 0

    # build solutions for all sums from 1 to S

    for s in range(1, S + 1):
        for c in coins:
            if s - c >= 0 and best[s - c] + 1 < best[s]:
                best[s] = best[s - c] + 1
                last[s] = c

    # if target sum cannot be formed
    if best[S] == big:
        return None, []

    # reconstruct solution by following last[] backwards
    used = []
    s = S
    while s > 0:
        used.append(last[s])
        s -= last[s]

    return best[S], used


coins = [1, 3, 4]
S = 6

cnt, sol = min_coins_dp(S, coins)

print(cnt)      # minimum number of coins
print(sol)      # one optimal set of coins 

'''
- correctness: 
    best[s] stores the minimum number of coins needed to form sum s.
    The recurrence considers all possible last coins c, and uses the optimal solution for s - c.
    By optimal substructure, this produces an optimal solution for every s.
    The solution is correctly reconstructed using the last[] array.

- time complexity: Θ(S⋅n)
- space complexity: Θ(S)

- remarks:
    - uses dynamic programming (bottom-up).
    - guarantees an optimal solution where greedy may fail.
    - assumes all coin values are positive integers.
'''