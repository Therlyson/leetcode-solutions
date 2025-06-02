from typing import List 

#problem 77 leetcode
def combine(n: int, k: int) -> List[List[int]]:
    output = []

    def bt(partial):
        if len(partial) == k:
            output.append(partial.copy())
        else:
            first_elem = 1 if len(partial)==0 else partial[-1]+1
            for i in range(first_elem, n+1):
                if(len(partial)+(n+1)-i < k): 
                    break
                bt(partial + [i])
    bt([])
    return output

print(combine(4, 2))