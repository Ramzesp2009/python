nums = [2,7,11,15]
target = 9
# nums = [3,2,4]
# target = 7
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (i != j and nums[i] + nums[j] == target):
                    return [i, j]
        return []



# with hash-table

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numMap = {}
#         n = len(nums)
#
#         # Build the hash table
#         for i in range(n):
#             numMap[nums[i]] = i
#
#         # Find the complement
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in numMap and numMap[complement] != i:
#                 return [i, numMap[complement]]
#
#         return []  # No solution found


solution = Solution()
print(solution.twoSum(nums, target))