"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
from collections import deque
class Solution_bfs:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.

    """
    def topSort(self, graph):
        # get node's in degree
        indegree = self.get_indegree(graph)
        start_node =[start for start in indegree.keys() if indegree[start]==0]

        queue = deque(start_node)

        orders =[]
        while queue:
            node = queue.popleft()

            orders.append(node)


            for nb in node.neighbors:
                indegree[nb]-=1
                if indegree[nb]==0:
                    queue.append(nb)

        return orders


"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution_dfs:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # build the indegree dict
        indegree ={x:0 for x in graph}
        for x in graph:
            for n in x.neighbors:
                indegree[n]+=1

        ret=[]
        #find out the start node first
        starts = [n for n in graph if indegree[n]==0]

        #dfs start from the node whose indegree is zero and recursive call it
        for start_n in starts:
            self.dfs(indegree,start_n,ret)

        return ret

    def dfs(self,indegree,nd,ret):
        ret.append(nd)
        indegree[nd]-=1

        for nb in nd.neighbors:
            indegree[nb]-=1
            if indegree[nb]==0:
                    self.dfs(indegree,nb,ret)







    def get_indegree(self,graph):

        node_to_degree={x:0 for x in graph}

        for node in graph:
            for nb in node.neighbors:
                node_to_degree[nb]+=1

        return node_to_degree
