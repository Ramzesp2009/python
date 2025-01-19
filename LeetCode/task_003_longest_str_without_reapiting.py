# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest
# substring without repeating characters.
# s = "pwwkew"
# s = "bbbbb"
# s = "pwwkyew"
s = "aab"
# s = 'asdrcvvcssaeelijndeh'
leer_list = []


class Solution:
    def lengthstring(self, s: str) -> int:
        result = []
        for i in s:
            if i not in leer_list:
                leer_list.append(i)
            else:
                if len(result) < len(leer_list):
                    result.clear()
                    result = leer_list[:]
                leer_list.clear()
        else:
            if len(result) < len(leer_list):
                result.clear()
                result = leer_list[:]
        return len(result)


solution = Solution()
print(solution.lengthstring(s))