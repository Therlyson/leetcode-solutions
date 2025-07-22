def maxProfit(prices: list[int]) -> int:
    max_output = 0
    l, r = 0, 1

    while r < len(prices):
        if prices[r] > prices[l]:
            value = prices[r] - prices[l]
            max_output = max(max_output, value)
        else:
            l = r
        r += 1
    return max_output

print(maxProfit([7, 1, 5, 3, 6, 4]))  # Example usage