class Solution:
    # @param {int[]} nums a set of distinct positive integers
    # @return {int[]} the largest subset
    def largestDivisibleSubset(self, nums):
        # dp
        import pdb
        #pdb.set_trace()
        n = len(nums)
        dp = [1] * n
        father = [-1] * n

        nums.sort()
        m, index = 0, -1
        for i in range(n):
            #print('i',i)
            for jj in range(i):
                #print('jj',jj)
                if nums[i] % nums[jj] == 0:
                    print(nums[i],nums[jj])
                    if 1 + dp[jj] > dp[i]:
                        dp[i] = dp[jj] + 1
                        father[i] = jj
                        print(father)
                #print(nums[i],nums[jj])

            print('##########')
            print('dp',dp)
            print('father',father)
            if dp[i] >= m:
                m = dp[i]
                index = i
                print('m',m)
                print('index',index)

        result = []
        print(father)
        for i in range(m):

            result.append(nums[index])
            print('index',index)
            print('result',result)
            index = father[index]

        return result

nums=[1,2,4,8]
s=Solution()

print(s.largestDivisibleSubset(nums))
