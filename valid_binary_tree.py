class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    bst inorder traverse is a sorted array
    """
    def isValidBST(self, root):
        self.lastnode=None
        self.isvalid = True
        self.inorder_trav(root)
        return self.isvalid

    def inorder_trav(self,root):
        if root is None:
            return
        self.inorder_trav(root.left)
        if self.lastnode is not None and self.lastnode.val>=root.val:
            self.isvalid=False
            return
        self.lastnode = root

        self.inorder_trav(root.right)


import sys
class Solution2:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    define the low boud and the right bound value ,and the two values are passed
    into the function from the last recursion
    """
    def isValidBST(self, root):
        if root is None:
            return True
        return self.boundBST(root,-sys.maxsize,sys.maxsize)

    def boundBST(self,root,low,up):
        if root is None:
            return True
        if root.val >= up or root.val <= low:
            return False

        return  self.boundBST(root.left,low,root.val) and self.boundBST(root.right,root.val,up)
