class Solution:
    def myAtoi(self, s: str) -> int:
        s.lstrip()
        # sing = 1
        if s[0] == '-':
            sign = -1
        else:
            sign = 1
        if s[0] in ['-', '+']:
            s = s[1:]
        digits = ''
        for char in s:
            if char.isdigit():
                digits += char
            else:
                break
        num = int(digits) if digits else 0
        num *= sign
        num = max(-2**31, min(num, 2**31 - 1))
        return num




solution = Solution()
print(solution.myAtoi('-012'))
print(solution.myAtoi('1337c0d3'))
print(solution.myAtoi(' -042'))
print(solution.myAtoi('0-1'))
print(solution.myAtoi("words and 987"))


