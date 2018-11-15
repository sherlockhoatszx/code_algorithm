class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        if A is None or len(A)==0:
            return 0

        farthest=A[0]

        for i in range(len(A)):
            if A[i]+i>=farthest:
                farthest=A[i]+i

        return farthest>len(A)-1
