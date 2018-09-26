"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    thinking_log: dfs traverse the tree, in recursive way,
    if the node is none ,then pop from stack, so,use a list to store the
    current path ,and meet the node.right and node.left isNone ,append to the
    result and pop
    """
        def binaryTreePaths(self, root):
        # write your code here
        if root is None:
            return []

        result=[]
        #to store the current path for recursive back
        #self.path =[]

        self.dfs(root,[],result)

        return result

    def dfs(self,node,path,result):
        path.append(str(node.val))

        if node.left is None and node.right is None:
            result.append('->'.join(path))
            #recuseive pop the end node
            path.pop()
            return
        if node.left:
            self.dfs(node.left,path,result)
        if node.right:
            self.dfs(node.right,path,result)
        #delete the leaf node from the stack,and if left and right
        #is none or have already been traversed,back 2
        path.pop()
