import heapq
from typing import List

#problem 2500 leetcode
def deleteGreatestValue(grid: List[List[int]]) -> int:
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            grid[i][j] = -grid[i][j]
        heapq.heapify(grid[i])

    maiorGeral = 0
    soma = 0
    while len(grid[0]) != 0:
        for sublista in grid:
            maior = -heapq.heappop(sublista)
            if maior>maiorGeral:
                maiorGeral = maior
        soma += maiorGeral
        maiorGeral = 0
    return soma

print(deleteGreatestValue([[1,2,4],[3,3,1]]))


#solução alternativa sem usar heapq
def deleteGreatestValue2(grid: List[List[int]]) -> int:
    maiorGeral = 0
    soma = 0

    while(len(grid[0]) > 0):
        for sublista in grid:
            maximo = max(sublista)
            sublista.remove(maximo)
            if maximo>maiorGeral:
                maiorGeral = maximo
        soma += maiorGeral
        maiorGeral = 0
    return soma