class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack=[]
        #辅助stack
        self.min_stack=[]

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        
        self.stack.append(number)
        if not self.min_stack or number <= self.min_stack[-1]:
            self.min_stack.append(number)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack:
            return -1
        number = self.stack.pop()
        if number==self.min_stack[-1]:
            self.min_stack.pop()
        return number

    """
    @return: An integer
    """
    def min(self):
        # write your code here
        return self.min_stack[-1]
