from typing import List, Any
import random, math

def algorithm_R(stream: List[Any], k: int, queries: List[int]) -> List[Any]:
    #queries 0 means query the reservoir after the 0th index of stream is processed
    result = [None] * len(queries) #will hold the result of the queries
    reservoir = [None] * k
    qi = 0 #index in the queries list
    while queries[qi] + 1 < k: #processing the queries before reservoir is fully initialized
        qi += 1

    for i, element in enumerate(stream):
        if i < k: #fill the reservoir with k elements
            reservoir[i] = element
            if qi != len(queries) and queries[qi] == i == k - 1:
                result[qi] = reservoir[:]
                qi += 1
        else:
            r = random.randint(0, i)
            if r < k:
                reservoir[r] = element #insert element with k / (i + 1) probability
            if qi != len(queries) and queries[qi] == i:
                result[qi] = reservoir[:] #if there is a query, reservoir is the answer
                qi += 1

    return result

#The optimal algorithm for reservoir sampling
def algorithm_L(stream: List[Any], k: int, queries: List[int]) -> List[Any]:
    #queries 0 means query the reservoir after the 0th element in stream is processed
    #Makes the random.random() work on the interval (0, 1)
    def open_random() -> float:
        x = random.random()
        while not x:
            x = random.random()
        return x

    result = [None] * len(queries)
    reservoir = [None] * k
    qi = 0 #index in the queries list
    while qi < len(queries) and queries[qi] + 1 < k: #answering the queries that happen before the reservoir is fully initialized
        qi += 1

    for i in range(k): #initializing the reservoir
        reservoir[i] = stream[i]

    _max = open_random() ** (1/k)
    while i < len(stream):
        i += int(math.log(open_random()) / math.log(1 - _max)) + 1 #geometric distribution
        while qi < len(queries) and queries[qi] < i: #answering previous queries
            result[qi] = reservoir[:]
            qi += 1
        if i < len(stream): #updating the reservoir and max variable
            reservoir[random.randrange(k)] = stream[i]
            _max *= open_random() ** (1 / k)

    return result