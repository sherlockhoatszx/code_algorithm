class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        prefix_hash = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            print(num)
            prefix_sum += num
            print(prefix_hash)
            if prefix_sum in prefix_hash:
                return prefix_hash[prefix_sum] + 1, i
            prefix_hash[prefix_sum] = i

        return -1, -1


testnums =[-3, -1,1, 2, -3, 4]
import pdb

s=Solution()
print(s.subarraySum(testnums))
