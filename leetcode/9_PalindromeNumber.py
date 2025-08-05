class Solution(object):
    def isPalindrome(self, x):
        list_ = list(str(x))
        list_len = len(list_)
        middle = list_len//2
        for i in range(middle):
            start = list_[i]
            end = list_[list_len - i - 1]
            if start != end:
                return False

        return True

sols = Solution()
print(sols.isPalindrome(123321))
