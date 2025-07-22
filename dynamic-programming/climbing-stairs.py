def climbStairs(n: int) -> int:
    memo = {}

    def step(n, memo={}):
        if n == 1:
            return 1
        if n == 2:
            return 2 
        value = memo.get(n)         
        if value is None:
            result = step(n-1, memo) + step(n-2, memo)
            memo[n] = result
            return result
        else:
            return memo.get(n)

    return step(n, memo)

print(climbStairs(5))  # Example usage