from typing import List, Any
import random

def reservoir_sampling(stream: List[Any], k: int, queries: List[int]) -> List[Any]:
    result = [] #will hold the result of the queries

    reservoir = []
    qi = 0 #index in the queries list
    for i, element in enumerate(stream):
        if i < k: #fill the reservoir with k elements
            reservoir.append(element)
            if qi != len(queries) and queries[qi] == i:
                result.append([])
                qi += 1
        else:
            r = random.randint(0, i)
            if r < k:
                reservoir[r] = element #insert element with k / (i + 1) probability
            if qi != len(queries) and queries[qi] == i:
                result.append(reservoir[:]) #if there is a query, reservoir is the answer
                qi += 1

    return result
