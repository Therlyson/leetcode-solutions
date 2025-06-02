import heapq

#problem 264 leetcode
def nthUglyNumber(n: int) -> int:
    prev = 0
    minha_lista_heap = [1]
    count = 0

    while(count < n):
        menor = heapq.heappop(minha_lista_heap)
        if(menor == prev):
            continue # Pula este número porque já foi processado
        count+=1
        heapq.heappush(minha_lista_heap, menor*2)
        heapq.heappush(minha_lista_heap, menor*3)
        heapq.heappush(minha_lista_heap, menor*5)
        prev = menor
    return menor
print(nthUglyNumber(5))