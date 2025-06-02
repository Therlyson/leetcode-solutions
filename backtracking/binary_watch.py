from typing import List 

#problem 401 leetcode
def readBinaryWatch(turnedOn: int) -> List[str]:
    output = []
    
    for h in range(12):
        h_leds = h.bit_count() #retorna o número de bits 1 no valor binário de um número inteiro.
        for m in range(60):
            m_leds = m.bit_count()
            total_leds = h_leds + m_leds

            if total_leds == turnedOn:
                time = f"{h}:{m:02d}"
                output.append(time)
    return output

print(readBinaryWatch(2)) 