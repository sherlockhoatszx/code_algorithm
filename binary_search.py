class Solution:
    '''implement the binary search algorithms,including naive version and
    a more advanced version'''
    def __init__(self,lst):
        self.lst = lst
        self.left=0
        self.right=len(lst)-1

    def naive_binary_search(self,target):
        '''but cannot solve last position target'''
        while self.left < self.right:
            mid = self.left + (self.right - self.left) //2
            if self.lst[mid] == target:
                print('found at',mid)
                #self.left=mid #to solve the last position target
                return mid


            elif self.lst[mid]<target:
                self.left = mid+1
            else:
                self.right = mid-1
        if self.lst[self.left]==target:
            return self.left
        return 'no'
    def last_position_binary_search(self,target):

        if not self.lst or target is None:
            return -1
        # avoid[1,1],t=1
        while self.left+1<self.right:
            # avoid 2^31 int,stack overflow
            mid = self.left + (self.right-self.left)//2

            if self.lst[mid]==target:
                self.left = mid
            elif self.lst[mid]<target:
                #avoid mid+1 mid-1 comfuse you
                self.left=mid
            else:
                self.right=mid
        if self.lst[self.right]==target:
            return self.right
        if self.lst[self.left]==target:
            return self.left
        return -1

    def first_position_binay_search(self,target):
        if not self.lst or target is None:
            return -1
        # avoid[1,1],t=1
        while self.left+1<self.right:
            mid = self.left + (self.right-self.left)//2

            if self.lst[mid]==target:
                self.right = mid
            elif self.lst[mid]<target:
                self.left=mid
            else:
                self.right=mid
        if self.lst[self.left]==target:
            return self.right
        if self.lst[self.right]==target:
            return self.left
        return -1






s = Solution('111234456')
s.naive_binary_search('1')
last_p = s.last_position_binary_search('1')
print('last position at',last_p)
first_p = s.first_position_binay_search('1')
print('first postion at',first_p)
