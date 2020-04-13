# basic version
class UnionFind:
    def __init__(self, n):
        self.father = list(range(n))
        # self.father = {}

    def find(self, x):
        if x == self.father[x]:
            return self.father[x]
        self.father[x] = self.find(self.father[x]) # path compression
        return self.father[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.father[px] = py
        