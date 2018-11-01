class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.arr=[None]*n
        self.head,self.tail = 0,-1
        self.size = n



    """
    @return:  return true if the array is full
    """
    def isFull(self):
        return self.arr[self.tail] is None


    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):

        return self.arr[self.tail] is None


    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self,element):

        self.tail = (self.tail+1)%self.size
        self.arr[self.tail] =element


    """
    @return: pop an element from the queue
    """
    def dequeue(self):

        elm = self.arr[self.head]
        self.arr[self.head] =None
        self.head =（self.head+1)%self.size
        return elm

s=Solution(5)
s.enqueue(1)
print(s.isEmpty())
