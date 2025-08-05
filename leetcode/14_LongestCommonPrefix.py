class Solution(object):
    def longestCommonPrefix(self, strs: list[str]):
        strs.sort()
        list_res = []
        list_first = list(strs[0])
        list_last = list(strs[-1])
        for i in range(len(list_first)):
            if list_first[i] == list_last[i]:
                list_res.append(list_first[i])
            else:
                break

        return "".join(list_res)




sols = Solution()
print(sols.longestCommonPrefix(["flower","flow","flight"]))