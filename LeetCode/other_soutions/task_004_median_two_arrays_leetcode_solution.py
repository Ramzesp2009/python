nums1 = [4, 3, 7, 9]
nums2 = [1, 7]


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new_num_list = nums1 + nums2
        new_num_list.sort()

        n = len(new_num_list)
        if n % 2 == 0:
            return (new_num_list[n // 2] + new_num_list[n // 2 - 1]) / 2
        else:
            return new_num_list[n // 2]

solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))