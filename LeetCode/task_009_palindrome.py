class Solution:
    def isPalindrome(self, x: int):
        return str(x) == str(x)[::-1]


sol = Solution()
print(sol.isPalindrome(12121))
