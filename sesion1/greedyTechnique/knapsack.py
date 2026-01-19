'''
- You have items with value and weight
- The backpack has a maximum capacity
- You are allowed to take fractions of items
- For each item, compute value / weight
- This tells you how valuable 1 unit of weight is
- Sort items from highest to lowest value/weight
- Always take the best item first
- If the whole item fits → take it
- If it doesn't fit → take only the part that fits
- Stop when the backpack is full
'''


def fractional_knapsack(items, capacity):
    # items = list of [value, weight]

    # compute value/weight ratio manually
    ratios = []
    for item in items:
        value = item[0]
        weight = item[1]
        ratio = value / weight
        ratios.append([ratio, value, weight])

    # sort ratios in descending order (simple sort)
    ratios.sort(reverse=True)

    total_value = 0.0

    for item in ratios:
        value = item[1]
        weight = item[2]

        if capacity == 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity = 0

    return total_value


# Example
items = [
    [60, 10],
    [100, 20],
    [120, 30]
]

capacity = 50
print(fractional_knapsack(items, capacity))
