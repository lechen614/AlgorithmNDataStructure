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

# path compression and union by rank can reduce Tree Height, ensure optimal time complexity
class UnionFind2:
    def __init__(self, n):
        self.father = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if x == self.father[x]:
            return self.father[x]
        self.father[x] = self.find(self.father[x]) # path compression
        return self.father[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if self.rank[px] > self.rank[py]:
            self.father[py] = px
        if self.rank[px] < self.rank[py]:
            self.father[px] = py
        if self.rank[px] == self.rank[py]:
            self.father[px] = py
            self.rank[py] += 1


# with distince sets count
class UnionFind3:
    def __init__(self, n):
        self.father = list(range(n))
        self.count = n

    def find(self, x):
        if x == self.father[x]:
            return self.father[x]
        self.father[x] = self.find(self.father[x]) # path compression
        return self.father[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.count -= 1 # count minus one
            self.father[px] = py

# count the size of all sets
class UnionFind4:
    def __init__(self, n):
        self.father = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if x == self.father[x]:
            return self.father[x]
        self.father[x] = self.find(self.father[x]) # path compression
        return self.father[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.father[px] = py
            self.size[py] += self.size[px]