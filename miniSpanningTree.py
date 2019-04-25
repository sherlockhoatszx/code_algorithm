'''difficult,kruskal algorithm'''


class Solution:
    # @param {Connection[]} connections given a list of connections
    # include two cities and cost
    # @return {Connection[]} a list of connections from results
    def lowestCost(self, connections):
        # Write your code here
        if connections is None or len(connections) == 0:
            return []

        connections.sort(key=lambda x: (x.cost, x.city1, x.city2))
        self.initialize(connections)

        results = []
        for connection in connections:
            city1 = connection.city1
            city2 = connection.city2
            if self.union(city1, city2):
                results.append(connection)

        if self.count != len(self.father) - 1:
            return []
        return results


    def initialize(self, connections):
        self.father = {}
        self.count = 0
        for connection in connections:
            city1 = connection.city1
            city2 = connection.city2
            if city1 not in self.father:
                self.father[city1] = city1
            if city2 not in self.father:
                self.father[city2] = city2

    def union(self, city1, city2):
        root_1 = self.find(city1)
        root_2 = self.find(city2)
        if root_1 != root_2:
            self.father[root_1] = root_2
            self.count += 1
            return True
        return False

    def find(self, city):
        path = []
        while self.father[city] != city:
            path.append(city)
            city = self.father[city]
        for p in path:
            self.father[p] = city
        return city
