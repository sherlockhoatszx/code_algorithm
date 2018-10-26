class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        from queue import Queue
        self.q=Queue()
        self.size=size
        self.sum=0.0



    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        self.sum +=val

        if self.q.qsize()==self.size:
            self.sum -= self.q.get()

        self.q.put(val)

        return self.sum*1.0/self.q.qsize()


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
