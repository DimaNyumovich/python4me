class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        is_need_plus_1 = False
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                digits[i] = digits[i] + 1
            if is_need_plus_1:
                digits[i] = digits[i] + 1
                is_need_plus_1 = False
            if digits[i] > 9:
                digits[i] = 0
                is_need_plus_1 = True
        if digits[0] == 0:
            digits = [1] + digits
        return digits


sol = Solution()
print(sol.plusOne([9, 8, 9]))