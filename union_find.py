'''The UnionFind has 2 navie impplementations,
first is first find:update the idx_path array each update
second is fast uion: Only update the element which need to union,and update its
value,father[father[p]]
third, WeightedQuickUnion, which will take the rank of each tree into consideration
to avoid unbalanced,and only update the union's 2 elements'''

class WeightedQuickUnion(object):

    def __init__(self,n):
        self.count = n
        self.id=[i for i in range(n)]
        self.sz = [1]*n

    def connected(self,p,q):
        return self.find(p) == self.find(q)

    def find(self,p):
        while (p != self.id[p]):
            #compression
            self.id[p]=self.id[self.id[p]]
            p = self.id[p]
        return p

    def union(self,p,q):
        #weighted union
        idp = self.find(p)
        print ("id of %d is: %d" % (p,idp))
        idq = self.find(q)
        print ("id of %d is: %d" % (q,idq))
        if not self.connected(p,q):
            print ("Before Connected: tree size of %d's id is: %d" % (p,self.sz[idp]))
            print ("Before Connected: tree size of %d's id is: %d" % (q,self.sz[idq]))
            if (self.sz[idp] < self.sz[idq]):
                print ("tree size of %d's id is smaller than %d's id" %(p,q))
                print ("id of %d's id (%d) is set to %d" % (p,idp,idq))
                self.id[idp] = idq

                print ("tree size of %d's id is incremented by tree size of %d's id" %(q,p))
                self.sz[idq] += self.sz[idp]
                print ("After Connected: tree size of %d's id is: %d" % (p,self.sz[idp]))
                print ("After Connected: tree size of %d's id is: %d" % (q,self.sz[idq]))
            else:
                print ("tree size of %d's id is larger than or equal with %d's id" %(p,q))
                print ("id of %d's id (%d) is set to %d" % (q,idq,idp))
                self.id[idq] = idp
                print ("tree size of %d's id is incremented by tree size of %d's id" %(p,q))
                self.sz[idp] += self.sz[idq]
                print ("After Connected: tree size of %d's id is: %d" % (p,self.sz[idp]))
                print ("After Connected: tree size of %d's id is: %d" % (q,self.sz[idq]))

            self.count -=1






qf = WeightedQuickUnion(10)

print ("initial id list is %s" % (",").join(str(x) for x in qf.id))

list = [
        (4,3),
        (3,8),
        (6,5),
        (9,4),
        (2,1),
        (8,9),
        (5,0),
        (7,2),
        (6,1),
        (1,0),
        (6,7)
        ]

for k in list:
    p =  k[0]
    q =  k[1]
    print ("." * 10 + "unioning %d and %d"  % (p,q)  + "." * 10)
    qf.union(p,q)
    print ("%d and %d is connected? %s" % (p,q,str(qf.connected(p,q))))

print ("final id list is %s" % (",").join(str(x) for x in qf.id))
print ("count of components is: %d" % qf.count)


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
