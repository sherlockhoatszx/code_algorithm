'''
prerequisites:graph data structure and the BFS algorithm
BFS and DFS,2method

{0,1,2#1,2#2,2} got 3 nodes,2 spearate mark#。
clone a undirectedgraph,each node in the graph contains one label and a neighbors
list,
first node label is 0 ,and edges from 0 to node 1 and node2
second node label is 1,and edges from 1 to node 2
third node labels is 2,and edges from 2 to node 2(itself)

'''
from collections import deque
class Solution_bfs:
    def cloneGraph(self, node):
        root = node
        if node is None:
            return node

        #first use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getNodes(node)

        #second, store the old->new node mapping in a hash map
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)

        #third,copy neighbors(edges) from the list
        for node in nodes:
            new_node = mapping[node]
            for neighbor in node.neighbors:
                new_neighbor = mapping[neighbor]
                new_node.neighbors.append(new_neighbor)

        return mapping[root]

    def getNodes(self, node):
        #use bfs queue to store nodes
        q = collections.deque([node])
        result = set([node])
        while q:
            head = q.popleft()
            for neighbor in head.neighbors:
                if neighbor not in result:
                    #set.add,list.append
                    result.add(neighbor)
                    q.append(neighbor)
        return result

class Solution_dfs:
    def cloneGraph(self,node):
        pass
