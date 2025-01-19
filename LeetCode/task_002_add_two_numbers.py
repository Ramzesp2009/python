# 2. Add Two Numbers
# You are given two non-empty linked lists representing
# two non-negative integers. The digits are stored in reverse
# order, and each of their nodes contains a single digit. Add
# the two numbers and return the sum as a linked list
# You may assume the two numbers do not contain any leading zero,
# except the number 0 itself.

# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = [5,5,5]
l2 = [2,0,2]


class Solution():
    def sum_two_numbers(self, l1 : list[int], l2 : list[int]) -> list[int]:
        l1.reverse()
        l2.reverse()
        numbers_1 = int(''.join(map(str, l1)))
        numbers_2 = int(''.join(map(str, l2)))
        sum_numbers = numbers_1 + numbers_2
        l3 = [int(i) for i in str(sum_numbers)]
        l3.reverse()
        return l3


solution = Solution()
print(solution.sum_two_numbers(l1, l2))



