# Example 1:            Example 2:
# Input: x = 123        Input: x = -123
# Output: 321           Output: -321

class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        sing = '-'
        zero = 0
        if s[0] == sing:
            new_s = s[1:]
            res = int(sing + new_s[::-1])
            return res if (-2**31) <= res <= (2**31-1) else 0
        elif s[0] == zero:
            new_s = s[1:]
            res = int(new_s[::-1])
            return res if (-2**31) <= res <= (2**31-1) else 0
        else:
            res = int(s[::-1])
            return res if (-2**31) <= res <= (2**31-1) else 0


solution = Solution()
print(solution.reverse(1534236469))
