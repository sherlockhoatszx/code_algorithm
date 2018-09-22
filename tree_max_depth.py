class Solution_trav:
    '''tranverse and divide conqure method，both O(n) '''

    def maxdepth(self,root):


        self.max_depth = 1

        self.trav_depth(root,1)

        return max_depth

    def trav_depth(self,node,current_depth):

        if node is None:
            return

        self.max_depth = max(self.max_depth,current_depth)

        self.trav_depth(node.left,current_depth+1)
        self.trav_depth(node.right,current_depth+1)

class Solution_dvCq:

    def max_depth(self,root):
        if root is None:
            return 0



        left_depth = self.max_depth(root.left)
        right_depth = self.max_depth(root.right)

        return max(left_depth,right_depth)+1
