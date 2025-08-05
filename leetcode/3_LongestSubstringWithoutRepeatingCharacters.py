class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        if len(s) == 2 and s[0] != s[1]: return 2
        res_sof = s[0]
        start_ind = 0
        # end_ind = 1

        for i in range(1, len(s)):
            end_ind = i + 1

            res = s[start_ind:end_ind]
            if res.count(s[i]) > 1:

                start_ind += res.index(s[i]) + 1
                res = s[start_ind:end_ind]
            if len(res) > len(res_sof):
                res_sof = res

            # print(res)
        return len(res_sof)

sol = Solution()
print(sol.lengthOfLongestSubstring('pwwkew'))