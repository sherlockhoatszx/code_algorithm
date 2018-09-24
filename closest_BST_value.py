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
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if root is None:
            return
        self.compare =abs(target-root.val)
        self.match_node ='infs'
        self.compareValue(root,target)

        return self.match_node


    def compareValue(self,node,target):
        if node is None:
            return
        print(node.val)
        if abs(self.compare) >= abs(node.val-target):
            self.match_node = node.val
            self.compare = target-node.val



            if self.compare<0:
                self.compareValue(node.left,target)



            if self.compare>0:
                self.compareValue(node.right,target)

        else:
            if node.right and abs(node.right.val-target)>=abs(self.compare) \
            and abs(node.right.val-target)<=abs(node.val-target):
                self.match_node = node.right.val
                self.compare = target - node.right.val


'''this version ,{10,5,15,3,6,12,18,#,4,#,8} doesn't pass'''
