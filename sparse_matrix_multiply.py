class Solution:
    # @param {int[][]} A a sparse matrix
    # @param {int[][]} B a sparse matrix
    # @return {int[][]} the result of A * B
    def multiply(self, A, B):

        n = len(A)
        m = len(A[0])
        l = len(B[0])
        k = len(B)

        C = [[0 for _ in range(l)] for i in range(n)]

        for arow in range(n):
            for bcol in range(l):

                for n in range(m):
                    if A[arow][n]!=0:

                        C[arow][bcol] += A[arow][n] * B[n][bcol]
        return C



class Solution2:

    def multiply(self,A,B):
        arows=len(A)
        acols=len(A[0])
        brows=len(B)
        bcols=len(B[0])

        C=[[0 for _ in range(bcols)] for i in range(arows)]

        sparse_matrix=[]

        for bcol in range(bcols):
            col_dict={}

            for brow in range(brows):
                if B[brow][bcol]!=0:
                    col_dict[brow]=B[brow][bcol]

            sparse_matrix.append([col_dict])


        for arow in range(arows):
            for bcol in range(bcols):
                for n in range(acols) :
                    if A[arow][n]!=0 and n in sparse_matrix[bcol][0]:



                        C[arow][bcol]+=A[arow][n]*B[n][bcol]


        return C



        for row in range(aRow):
            for cl,rw in zip(aCol,bRow):
