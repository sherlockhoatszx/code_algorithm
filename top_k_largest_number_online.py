

import heapq

class Solution:
    '''online top k'''
    # @param {int} k an integer
    def __init__(self, k):
        # initialize your data structure here.
        self.k = k
        self.nums = []
        heapq.heapify(self.nums)

    # @param {int} num an integer
    def add(self, num):

        if len(self.nums) < self.k:
            heapq.heappush(self.nums, num)
        elif num > self.nums[0]:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, num)

    # @return {int[]} the top k largest numbers in array
    def topk(self):
        # Write your code here
        return sorted(self.nums, reverse=True)
