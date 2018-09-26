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
        #stack
        left_weight = self.helper(root.left)
        right_weight = self.helper(root.right)

        if left_weight + right_weight + root.val <= self.minumun_weight:
            self.minumun_weight = left_weight + right_weight + root.val
            self.result = root

        return left_weight + right_weight + root.val

class Solution:

    '''pure divide_conqure method'''

    def findSubtree(self, root):
        minimum, subtree, sum = self.helper(root)
        return subtree

    def helper(self, root):
        if root is None:
            return sys.maxsize, None, 0

        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.right)

        sum = left_sum + right_sum + root.val
        if left_minimum == min(left_minimum, right_minimum, sum):
            return left_minimum, left_subtree, sum
        if right_minimum == min(left_minimum, right_minimum, sum):
            return right_minimum, right_subtree, sum

        return sum, root, sum
