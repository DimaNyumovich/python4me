class Solution(object):
    def isPalindrome(self, x):
        open_brackets = ['(', '[', '{']
        close_brackets = [')', ']', '}']
        stack = []
        for item in x:
            if item in open_brackets:
                stack.append(item)
            elif item in close_brackets:
                if len(stack) == 0:
                    return False
                elif close_brackets.index(item) == open_brackets.index(stack[-1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False






sols = Solution()
print(sols.isPalindrome("(])"))