class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    recursive way first call root.left
    """
    def preorderTraversal(self, root):
        # ret should be out of the recursive method to store
        self.ret =[]
        self.pre_trav(root)
        return self.ret

    def pre_trav(self,root):
        if root is None:
            return

        self.ret.append(root.val)
        #keep left left left,meanwhile,put the node in a stack
        self.pre_trav(root.left)
        #call from the stack from bottom to top bottom.right,top-1.right,top-2.right
        #stack not expilicty
        self.pre_trav(root.right)

class Solution2:

    '''not recursive way, use stack to store the node
    push right and left, pop it'''

    def preorderTraversal(self, root):

        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder
