# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and
# n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Explanation: merged
# array = [1, 2, 3] and median is 2.
#
# Example 2:
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.50000
# Explanation: merged
# array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5.
from numpy import median


class Solution:
    def median_two_arrays(self, num_1: list[int], num_2: list[int]) -> float:
        result = num_1 + num_2
        # result.sort()
        return median(result)


def main():
    # num1 = [1, 3]
    # num2 = [2]
    num1 = [5, 9, 2]
    num2 = [3, 4]
    solution = Solution()
    print(solution.median_two_arrays(num1, num2))



if __name__ == "__main__":
    main()