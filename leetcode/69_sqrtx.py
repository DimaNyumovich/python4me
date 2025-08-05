class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x
        prev = 0
        if x == 1: return 1
        while True:
            next: int = (start + end) // 2
            res = next * next
            if res == x:
                return next
            if res == prev:
                if res > x:
                    return next - 1
                elif res < x:
                    return next
            prev = res

            if res < x:
                start = next
            elif res > x:
                end = next





sol = Solution()
print(sol.mySqrt(0))