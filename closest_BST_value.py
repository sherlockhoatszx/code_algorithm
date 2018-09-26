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
        #self.compare =abs(target-root.val)
        self.match_node =root.val
        self.compareValue(root,target)

        return self.match_node


    def compareValue(self,node,target):
        if node is None :

            return
        print(node.val)
        if abs(target-self.match_node) >= abs(node.val-target):
            self.match_node = node.val
            #self.compare = target-node.val



        #the below if condition shoule be the same level of the above 1
        if target<node.val and node.left:
            self.compareValue(node.left,target)
            if  abs(node.left.val-target)<abs(self.match_node-target) :
                self.match_node=node.left





        if target>node.val and node.right:
            print('in right')
            self.compareValue(node.right,target)
            if abs(node.right.val-target)< abs(self.match_node-target):
                self.match_node=node.right

'''log summary:1.not only compare with the current node,but also consider
current_node.left or current_node.right, 2,self.match_node as a global variable
to store the current node,3,the last 2 if condition should not be indent to the
above one '''


class Solution2:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        if not root:
            raise Exception

        lower = self.findLower(root, target)
        upper = self.findUpper(root, target)
        if lower and upper:
            if target - lower.val > upper.val - target:
                return upper.val
            else:
                return lower.val
        if lower:
            return lower.val
        if upper:
            return upper.val


    def findLower(self, root, target):
        curr = root
        last = None
        while curr:
            if curr.val <= target:
                last = curr
                curr = curr.right
            else:
                curr = curr.left
        return last  # may be None if no one <= target

    def findUpper(self, root, target):
        curr = root
        last = None
        while curr:
            if curr.val > target:
                last = curr
                curr = curr.left
            else:
                curr = curr.right
        return last  # may be None if no one > target
