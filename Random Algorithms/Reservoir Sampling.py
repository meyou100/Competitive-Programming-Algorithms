from typing import List, Any
import random, math

def algorithm_R(stream: List[Any], k: int, queries: List[int]) -> List[Any]:
    result = [None] * len(queries) #will hold the result of the queries

    reservoir = [None] * k
    qi = 0 #index in the queries list
    for i, element in enumerate(stream):
        if i < k: #fill the reservoir with k elements
            reservoir[i] = element
            if qi != len(queries) and queries[qi] == i:
                result[qi] = []
                qi += 1
        else:
            r = random.randint(0, i)
            if r < k:
                reservoir[r] = element #insert element with k / (i + 1) probability
            if qi != len(queries) and queries[qi] == i:
                result[qi] = reservoir[:] #if there is a query, reservoir is the answer
                qi += 1

    return result

def algorithm_L(stream: List[Any], k: int, queries: List[int]) -> List[Any]:
    result = [None] * len(queries)

    reservoir = [None] * k
    i = 0
    qi = 0 #index in the queries list
    while i < k:
        reservoir[i] = stream[i]

    _max = random.random() ** (1/k)
    while queries[qi] < k:
        qi += 1
        result[qi] = []

    while i < len(stream):
        i += int(math.log(random.random()) / math.log(1 - _max)) + 1
        if i < len(stream):
            reservoir[random.randrange(k)] = stream[i]
            _max *= random.random() ** (1 / k)

        if queries[qi] <= i:
            result[qi] = reservoir[:]

    return result