'''递归，分治法
At the top
LCA(3, 6, 8)  left 6, right 8 --> I am the the LCA : 3
LCA(3, 5, 4)  left 5, right nullptr --> what my left subtree returns is the LCA : 5
LCA(3, 1, 0)  left nullptr, right 1 --> what my right subtree returns is the LCA : 1
During the recursive call: LCA(2, 6, 0) --> left nullptr, right subtree nullptr --> I will return nullptr.
Base Case 1: root is nullptr --> return nullptr
Base Case 2: LCA(5, 5, 8) --> ignore everything under me, return myself
             LCA(5, 8, 5) --> ignore everything under me, return myself
o(n) time: In the worst case, traverse every node'''
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the lowest common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # A & 下面有B => A
        # B & 下面有A => B
        # A & 下面啥都没有 => A
        # B & 下面啥都有 => B
        if root is None:
            return None

        if root == A or root == B:
            return root

        left_result = self.lowestCommonAncestor(root.left, A, B)
        right_result = self.lowestCommonAncestor(root.right, A, B)

        # A 和 B 一边一个
        if left_result and right_result:
            return root

        # 左子树有一个点或者左子树有LCA
        if left_result:
            return left_result

        # 右子树有一个点或者右子树有LCA
        if right_result:
            return right_result

        # 左右子树啥都没有
        return None
