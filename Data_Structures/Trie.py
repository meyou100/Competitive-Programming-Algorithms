from typing import Callable

class Trie:
    class Node:
        __slots__ = 'end', 'next'
        def __init__(self, size: int=26) -> None:
            self.next = [-1] * size
            self.end = False

        def __repr__(self) -> str:
            return str(self.next)

    __slots__ = 'vertices', 'size', 'mapping'
    def __init__(self, *words: str, size: int=26, mapping: Callable[[str], int]=lambda a: ord(a) - 97) -> None:
        self.vertices = [self.Node(size)]
        self.size = size
        self.mapping = mapping
        for word in words:
            self.add(word)

    def add(self, word: str) -> None:
        vertex = self.vertices[0]
        for letter in word:
            ind = self.mapping(letter)
            if vertex.next[ind] == -1:
                vertex.next[ind] = len(self.vertices)
                self.vertices.append(self.Node(self.size))
            vertex = self.vertices[vertex.next[ind]]
        vertex.end = True

    def __contains__(self, word: str) -> bool:
        vertex = 0
        for letter in word:
            vertex = self.vertices[vertex].next[self.mapping(letter)]
            if vertex == -1:
                return False
        return self.vertices[vertex].end

    def __delitem__(self, word: str) -> bool:
        #deletes the word from the trie including intermediate nodes, returning true if successful
        vertex = 0
        stack = []
        for letter in word:
            ind = self.mapping(letter)
            stack.append((vertex, ind))
            vertex = self.vertices[vertex].next[ind]
            if vertex == -1:
                return False

        if self.vertices[vertex].end:
            self.vertices[vertex].end = False
            if any(map(lambda a: a != -1, self.vertices[vertex].next)):
                return True
            vertex, ind = stack.pop()
            while sum(map(lambda a: a != -1, self.vertices[vertex].next)) == 1:
                vertex, ind = stack.pop()
            self.vertices[vertex].next[ind] = -1
            return True
        return False

    def delete_end(self, word: str) -> bool:
        #updates the end of the word to false, returning true if successful
        vertex = 0
        for letter in word:
            vertex = self.vertices[vertex].next[self.mapping(letter)]
            if vertex == -1:
                return False
        if self.vertices[vertex].end:
            self.vertices[vertex].end = False

            return True
        return False

    def is_prefix(self, word: str) -> bool:
        vertex = 0
        for letter in word:
            vertex = self.vertices[vertex].next[self.mapping(letter)]
            if vertex == -1:
                return False
        return True

t = Trie('hello', 'hi', 'abc')
print(t.vertices, len(t.vertices))
del t['hello']
print(t.vertices, len(t.vertices))