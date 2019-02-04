class UnionFind:
    """ With Path Compression, beats 93.60%
    """
    def __init__(self, N):
        self.components = N
        self.id = [i for i in range(N)]
        self.sz = [1 for _ in range(N)]

    def root(self, p):
        while self.id[p] != p:
            self.id[p] = self.id[self.id[p]] #此句删掉就没有Path Compression
            p = self.id[p]
        return p

    def find(self, p, q):
        i = self.root(p)
        j = self.root(q)
        return i == j

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        elif i < j:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

        self.components -= 1

class WeightedUnionFind:
    """ Weighted Union Find, beats 55.00%
    """
    def __init__(self, N):
        self.components = N
        self.id = [i for i in range(N)]
        self.sz = [1 for _ in range(N)]

    def root(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def find(self, p, q):
        i = self.root(p)
        j = self.root(q)
        return i == j

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j:
            return
        elif i < j:
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]

        self.components -= 1

class QuickUnion:
    """ Quick Union, beats 28.02%
    """
    def __init__(self, N):
        self.components = N
        self.id = [i for i in range(N)]

    def root(self, p):
        while self.id[p] != p:
            p = self.id[p]
        return p

    def find(self, p, q):
        i = self.root(p)
        j = self.root(q)
        return i == j

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        if i == j: return
        self.id[i] = j
        self.components -= 1
'''
class QuickFind:
    """ Quick Find, beats 0.02%
    """
    def __init__(self, N):
        self.components = N
        self.id = [i for i in range(N)]

    def find(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        if self.find(p, q): return
        for i in range(self.sz):
            if self.find(i, p):
                self.id[i] = self.id[q]
        self.components -= 1
 '''
class Solution:

    def validTree(self, n, edges):

        if len(edges) != n - 1: return False

        unionFind = UnionFind(n) # weighted union find with path compression
        """
        unionFind = WeightedUnionFind(n)     # union find without path compression
        unionFind = QuickUnion(n)			# quick union method
        unionFind = QuickFind(n)			# quick find method
        """

        for edge in edges:
            unionFind.union(edge[0], edge[1])

        return unionFind.components == 1
