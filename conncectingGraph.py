class ConnectingGraph1:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.sz =[1]*(n+1)
        self.father = {}
        for i in range(1,n+1):
            self.father[i] = i

    def connect(self, p, q):
        """
        @param: p: An integer
        @param: q: An integer
        @return: nothing
        """
        idp = self.find(p)
        idq = self.find(q)
        if not self.query(p,q):
            if (self.sz[idp] < self.sz[idq]):
                self.father[idp] = idq
                self.sz[idq] += self.sz[idp]
            else:
                self.father[idq] = idp
                self.sz[idp] += self.sz[idq]


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
            node = self.father[node]
        return node
