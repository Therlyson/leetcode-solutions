from typing import List

#problem 1046 leetcode

#primeira ideia básica
def lastStoneWeight(stones: List[int]) -> int:
    stones.sort(reverse=True)
    while len(stones) > 1:
        first = stones.pop(0)
        second = stones.pop(0)
        if first != second:
            resto = abs(first - second)
            stones.append(resto)
            stones.sort(reverse=True)
    return stones[0] if stones else 0

# print(lastStoneWeight([2,7,4,1,8,1]))


#segunda ideia com heap
import heapq
def lastStoneWeight2(stones: List[int]) -> int:
    for i in range(len(stones)):
        stones[i] = -stones[i]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = -heapq.heappop(stones)
        second = -heapq.heappop(stones)
        if first != second:
            resto = first - second
            heapq.heappush(stones, -resto)
    return -stones[0] if stones else 0

print(lastStoneWeight2([2,7,4,1,8,1]))