class Solution:
    def romanToInteger(self, s: str):
        res = []
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in s:
            res.append(rom[i])
        result = sum(res)
        if len(s) == 1:
            return result
        elif len(s) == 2:
            if res[0] < res[1]:
                result -= res[0] * 2
                return result
        for x in range(len(s)-1):
            if res[x] < res[x+1]:
                result -= res[x] * 2
        return result


if __name__ == '__main__':
    s = Solution()
    roman = 'D'
    r = s.romanToInteger(roman)
    print(r)
