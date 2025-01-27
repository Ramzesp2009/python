class Solution:
    def romanToInteger(self, num: int):
        res = 0
        new_str = num[::-1]
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(num)):
            if i == 1:
                if rom[new_str[i]] < rom[new_str[i -1]]:
                    res -= rom[new_str[i]]
                continue
            res += rom[new_str[i]]
        return res


if __name__ == '__main__':
    s = Solution()
    roman = 'XIX'
    r = s.romanToInteger(roman)
    print(r)
