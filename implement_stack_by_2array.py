class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        from queue import Queue
        self.que1 = Queue()
        self.que2 = Queue()


    def push(self, x):
        # write your code here

        self.que1.put(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while self.que1.qsize()>1:
            self.que2.put(self.que1.get())
        item = self.que1.get()
        self.que1,self.que2 = self.que2,self.que1

        return item

    """
    @return: An integer
    """
    def top(self):
        # write your code here

        while self.que1.qsize()>1:
            self.que2.put(self.que1.get())

        item = self.que1.get()
        self.que1,self.que2 = self.que2,self.que1
        self.que1.put(item)

        return item



    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here

        return self.que1.empty()
