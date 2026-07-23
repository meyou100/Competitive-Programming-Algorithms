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
    #queries 0 means query the reservoir after the 0th index of stream is processed
    #Makes sure the random function doesn't produce 0
    def open_random() -> float:
        x = random.random()
        while not x:
            x = random.random()
        return x

    result = [None] * len(queries)
    reservoir = [None] * k
    i = 0
    qi = 0 #index in the queries list
    while i < k: #initializing the reservoir
        reservoir[i] = stream[i]
        i += 1
    i -= 1 #i must equal k - 1 for the while loop to work
    while qi < len(queries) and queries[qi] + 1 < k: #answering the queries that happen before the reservoir is fully initialized
        qi += 1

    _max = open_random() ** (1/k)
    while i < len(stream):
        i += int(math.log(open_random()) / math.log(1 - _max)) + 1
        while qi < len(queries) and queries[qi] < i:
            result[qi] = reservoir[:]
            qi += 1
        if i < len(stream):
            reservoir[random.randrange(k)] = stream[i]
            _max *= open_random() ** (1 / k)

        print(i, reservoir, qi)
    return result
print(algorithm_L(list(range(6)), 5, queries=[0,1,2,3,4,5]))



print(algorithm_R(list(range(1000)), k=5, queries=[0,1,2,3,4,5,999]))