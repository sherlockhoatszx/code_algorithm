class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # write your code here
        #init a stack
        stack=[]
        #traverse tokens from left to right
        for tk in tokens:
            #if token is number,add to stack
            if tk.isdigit():
                stack.append(int(tk))
            #if token is operator
            else:
            #这里没有区分一元操作符和二元操作符
                    op2 = stack.pop()
                    op1 = stack.pop()
                    if tk == '+': stack.append(op1 + op2)
                    elif tk == '-': stack.append(op1 - op2)
                    elif tk == '*': stack.append(op1 * op2)
                    else: stack.append(int(op1 * 1.0 / op2))

        return stack[0]
