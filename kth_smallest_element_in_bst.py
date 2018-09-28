"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        #left to bottom
        stack=[]
        while root.left:
            stack.append(root)
        for i in range(k):

            if stack[-1].right:
                node = stack[-1].right
                while node:
                    
                    node = node.left
                    stack.append(node)
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()

        return stack[-1].val
