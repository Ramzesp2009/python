class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        start, size = 0, 1
        for i in range(1, len(s)):
            left, right = i - size, i + 1

            s1 = s[left - 1 : right]
            s2 = s[left: right]

            if left - 1 >= 0 and s1 == s1[::-1]:
                start, size = left -1, size + 2
            elif s2 == s2[::-1]:
                start, size = left, size + 1

        return s[start: start + size]


solution = Solution()
print(solution.longestPalindrome('asdfdsasdf'))