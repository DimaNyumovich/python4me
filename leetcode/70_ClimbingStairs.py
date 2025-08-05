class Solution(object):
    def climbStairs1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0: return 1
        elif x == 1: return 1
        else:
            return self.climbStairs(x - 1) + self.climbStairs(x - 2)

    def climbStairs(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1: return 1
        a, b = 1, 1
        for _ in range(2, x + 1):
            a,b = b, a+b
        return b


sol = Solution()
print(sol.climbStairs1(4))
print('---------')
print(sol.climbStairs(4))