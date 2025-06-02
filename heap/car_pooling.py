from typing import List

#promblem 1094 leetcode

#primeira ideia básica
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    inicio = trips[0][1]
    fim = trips[0][2]
    for i in range(1, len(trips)):
        if trips[i][1] < inicio:
            inicio = trips[i][1]
        if trips[i][2] > fim:
            fim = trips[i][2]

    car = []
    
    for i in range(inicio, fim+1):
        for j in range(0, len(trips)): 
            if i == trips[j][2]: #chegou no destino
                car.remove(trips[j][0])
            if i == trips[j][1]: #entrou no carro
                car.append(trips[j][0])
        if sum(car) > capacity:
            return False
    return True


#segunda ideia com heap
import heapq
def carPooling2(trips: List[List[int]], capacity: int) -> bool:
    heap_saida = []
    qtd_passageiros = 0

    trips.sort(key=lambda x: x[1])
    for trip in trips:
        while heap_saida and heap_saida[0][0] <= trip[1]:
            destino = heapq.heappop(heap_saida)
            qtd_passageiros -= destino[1]
        heapq.heappush(heap_saida, (trip[2], trip[0], trip[1])) #saida, passageiros, entrada
        qtd_passageiros += trip[0]

        if qtd_passageiros > capacity:
            return False
    return True

# print(carPooling2([[2,1,5],[3,5,7]], 3))
# print(carPooling([[2,1,5],[3,3,7]], 5))
# print(carPooling([[2,1,5],[3,3,7]], 4))
# print(carPooling([[5,4,7],[7,4,8],[4,1,8]], 17))
# print(carPooling2([[4,5,6],[6,4,7],[4,3,5],[2,3,5]], 13))
print(carPooling2([[3,2,8],[4,4,6],[10,8,9]], 11))



