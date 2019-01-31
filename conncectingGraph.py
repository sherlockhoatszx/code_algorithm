class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.sz =[1]*(n+1)
        self.father = {}
        for i in range(1,n+1):
            self.father[i] = i

    def connect(self, a, b):
        """
        @param: p: An integer
        @param: q: An integer
        @return: nothing
        """
        ida = self.find(a)
        idb = self.find(b)
        if not self.query(a,b):
            if (self.sz[ida] < self.sz[idb]):
                self.father[ida] = idb
                self.sz[idb] += self.sz[ida]
            else:
                self.father[idb] = ida
                self.sz[ida] += self.sz[idb]


    def query(self, a, b):
        # write your code here
        """
        @param: a: An integer
        @param: b: An integer
        @return: A boolean
        """
        return self.find(a) == self.find(b)
    def find(self,node):
        while node != self.father[node]:
            self.father[node] = self.father[self.father[node]]
            node = self.father[node]
        return node
