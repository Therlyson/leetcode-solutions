def maxProfit(prices: list[int]) -> int:
    min_number = prices[0]
    max_output = 0
    
    for i in range(1, len(prices)):
        if (prices[i] - min_number) > max_output:
            value = prices[i] - min_number
            max_output = max(value, max_output)
        min_number = min(prices[i], min_number)
    return max_output

print(maxProfit([7, 1, 5, 3, 6, 4]))  # Example usage
        
# Em cada iteração o subproblema é resolvido para o dia i usando apenas os estados de i−1, sem reprocessar toda a lista. Isso é exatamente programação dinâmica.