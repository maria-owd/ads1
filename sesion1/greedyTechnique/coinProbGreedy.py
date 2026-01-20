'''
- Given coin values and a target sum
- Always choose the largest coin ≤ remaining sum
- Subtract its value from the sum
- Repeat until the sum becomes 0
- Fast and simple
- Not always optimal (fails for some coin sets)
'''

def greedy_coin_change(S, coins):
    coins.sort(reverse=True)
    used = []

    for c in coins:
        while S >= c:
            S -= c
            used.append(c)

    if S != 0:
        return None  # sum cannot be formed

    return used

# Example - that works
coins_1 = [1, 2, 5, 10]
s_1 = 18

# Example - that doesn't work
#coins_2 = [1, 3, 4]
#s_2 = 6
    # greedy -> 4 + 1 + 1 (3 coins)
    # optimal -> 3 + 3 (2 coins)

print(greedy_coin_change(s_1, coins_1))
#print(greedy_coin_change(s_2, coins_2))  
