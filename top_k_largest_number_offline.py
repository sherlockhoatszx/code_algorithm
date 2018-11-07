'''offline find topk,
obviously,there is also online algorithm
2method implmented:
1,heap
2,quicksort'''
#method 1,heap
import heapq

class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self, nums, k):
        # Write your code here
        heapq.heapify(nums)
        topk = heapq.nlargest(k, nums)
        topk.sort()
        topk.reverse()
        return topk

#method2, quicksort

import random

class Solution2:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
class Solution:
    '''
    @param {int[]} nums an integer array
    @param {int} k an integer
    @return {int[]} the top k largest numbers in array
    '''
    def topk(self,nums,k):
        self.quicksort(nums,0,len(nums)-1)
        topk=[]
        for i in range(1,k+1):
            topk.append(nums[-i])

        return topk




    def quicksort(self,nums,start,end):
        #if start>=k:
            #return

        if start>=end:
            return

        left,right=start,end
        pivot = nums[start+(end-start)//2]

        while left<=right:
            while left<=right and nums[left]<pivot:
                left+=1

            while left<=right and nums[right]>pivot:
                right-=1

            if left<=right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1

        self.quicksort(nums,start,right)

        self.quicksort(nums,left,end)


testarr=[3,10,1000,-99,4,100]
s=Solution2()
print(s.topk(testarr,2))
