class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {int} the minimun weight node
    '''like the code of maxdepth of a binary tree,there are also traverse and
    divide_conqure method'''

    def findSubtree(self, root):
        self.minumun_weight = sys.maxsize
    	self.result = None
        self.helper(root)

        return self.result

    def helper(self, root):
        if root is None:
            return 0

        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)

        if left_weight + right_weight + root.val <= self.minumun_weight:
            self.minumun_weight = left_weight + right_weight + root.val
            self.result = root

        return left_weight + right_weight + root.val
