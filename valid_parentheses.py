'''stack,#easy#'''

class Solution:

    def isValidParentheses(self,s):
        marks={'(':')','[':']','{':'}'}

        stack=[]

        for ch in s:
            if ch in marks:
                stack.append(ch)
            if ch in marks.values():
                if not stack:
                    return False
                if ch != marks[stack[-1]]:
                    return False

                stack.pop()
        return not stack
