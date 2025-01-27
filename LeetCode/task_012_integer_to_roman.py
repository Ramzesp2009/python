class Solution:
    def intToRoman(self, num: int):
        position = len(str(num))
        rom = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
               6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
               40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM',
               50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        res = []
        num = list(str(num))
        for i in range(position):
            digit = int(num.pop(0))
            if position > 3:
                for x in range(digit):
                    res.append(rom[1000])
            elif position == 3:
                if digit == 5:
                    res.append(rom[500])
                elif digit == 4:
                    res.append(rom[400])
                elif digit == 9:
                    res.append(rom[900])
                elif digit > 5:
                    res.append(rom[500])
                    for i in range(digit - 5):
                        res.append(rom[100])
                elif digit < 5:
                    for i in range(digit):
                        res.append(rom[100])
            elif position == 2:
                if digit == 5:
                    res.append(rom[50])
                elif digit == 4:
                    res.append(rom[40])
                elif digit == 9:
                    res.append(rom[90])
                elif digit > 5:
                    res.append(rom[50])
                    for i in range(digit - 5):
                        res.append(rom[10])
                elif digit < 5:
                    for i in range(digit):
                        res.append(rom[10])
            elif position == 1:
                if digit == 0:
                    break
                res.append(rom[digit])
            position -= 1
        return ''.join(res)


if __name__ == '__main__':
    solution = Solution()
    res = solution.intToRoman(773)
    print(res)