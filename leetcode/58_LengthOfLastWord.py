class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_ = s.split(' ')
        res = 0
        for item in list_:
            if item != '':
                res = len(item)
        return res

sol = Solution()
print(sol.lengthOfLastWord("   fly me   to   the moon  "))