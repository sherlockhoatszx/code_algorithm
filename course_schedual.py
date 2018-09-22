'''现在你总共有 n 门课需要选，记为 0 到 n - 1.
一些课程在修之前需要先修另外的一些课程，比如要学习课程 0 你需要先学习课程 1 ，表示为[0,1]
给定n门课以及他们的先决条件，判断是否可能完成所有课程？


样例
给定 n = 2，先决条件为 [[1,0]] 返回 true
给定 n = 2，先决条件为 [[1,0],[0,1]] 返回 false
首先将list of list变成边和入度的图表示方法。然后先去除入度为0的node,同时找到相连边的node,
node edges -1,如－1后有新的顶点入度变成0，就加入队列中'''

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here

        #change the prerequirement from list of list to the node_edges,indegree
        #Which are to represent the graph format

        edges = {i:[] for i in range(numCourses)}
        indegree = [0 for i in range(numCourses)]
        import queue
        for i,j in prerequisites:
            edges[j].append(i)
            indegree[i] += 1

        queue,count = queue.Queue(maxsize=numCourses),0

        for i,v in enumerate(indegree):
            if v==0:
                queue.put(i)

        while not queue.empty():
            node = queue.get()
            #error here
            count+=1

            for vex in edges[node]:
                indegree[vex]-=1
                if indegree[vex]==0:
                    queue.put(vex)

        return count==numCourses


s=Solution()

print(s.canFinish(2,[[1,0]]))
