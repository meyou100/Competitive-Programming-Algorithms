from typing import Callable

#persistent array, iterative instead of recursive
class Trie:
    class Node:
        __slots__ = 'parent', 'end', 'goto', 'exit_link', 'suf_link', 'next', 'parent_ch'
        def __init__(self, size: int=26, p: int=-1, pch: str='') -> None:
            self.next = [-1] * size
            self.end = False
            self.parent = p
            self.parent_ch = pch #stores the character representing the edge between p and this Node
            self.suf_link = -1
            self.goto = [-1] * size #precomputing where each next character will land
            self.exit_link = 0 #0 indicates not processed yet

        def __repr__(self) -> str:
            return self.parent_ch + str(self.parent) + str(self.next) + str(self.exit_link) + str(self.suf_link)

    __slots__ = 'size', 'vertices', 'mapping'
    def __init__(self, size: int=26, mapping: Callable[[str], int]=lambda a: ord(a) - 97) -> None:
        self.size = size
        self.vertices = [self.Node(size)]
        self.mapping = mapping #function to map characters to their proper index in the trie

    def add_string(self, s: str) -> None:
        #adds a string to the trie
        cur_vertex = 0 #start at the root
        for ch in s:
            ind = self.mapping(ch) #compute the index of Node.next that this character would be in
            if self.vertices[cur_vertex].next[ind] == -1:
                self.vertices[cur_vertex].next[ind] = len(self.vertices)
                self.vertices.append(self.Node(self.size, p=cur_vertex, pch=ch))
            cur_vertex = self.vertices[cur_vertex].next[ind]
        self.vertices[cur_vertex].end = True

    def get_suf_link(self, vertex: int) -> int:
        #finds the suffix link of the given vertex
        if self.vertices[vertex].suf_link == -1:
            if not vertex or not self.vertices[vertex].parent:
                self.vertices[vertex].suf_link = 0
            else:
                self.vertices[vertex].suf_link = self.go_to(self.get_suf_link(self.vertices[vertex].parent), self.vertices[vertex].parent_ch)
        return self.vertices[vertex].suf_link

    def go_to(self, vertex: int, ch: str) -> int:
        #finds the next vertex given the most recent character of the string
        ind = self.mapping(ch)
        if self.vertices[vertex].goto[ind] == -1:
            if self.vertices[vertex].next[ind] != -1:
                self.vertices[vertex].goto[ind] = self.vertices[vertex].next[ind]
            else:
                self.vertices[vertex].goto[ind] = self.go_to(self.get_suf_link(vertex), ch) if vertex else 0
        return self.vertices[vertex].goto[ind]

    def get_exit_link(self, vertex: int) -> int:
        #finds the nearest end vertex reachable from vertex by suffix links
        if not self.vertices[vertex].exit_link:
            if self.vertices[vertex].end:
                self.vertices[vertex].exit_link = vertex
            else:
                self.vertices[vertex].exit_link = self.get_exit_link(self.get_suf_link(vertex)) if vertex else -1
        return self.vertices[vertex].exit_link