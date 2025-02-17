class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        if len(nums) == 3:
            if sum(nums) == 0:
                res.append(nums)
                return res
            else:
                return res
        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    if nums[x]+nums[y]+nums[z] == 0:
                        res.append([nums[x],nums[y],nums[z]])
        for i in res:
            i.sort()
        res.sort()
        new_res = []
        for z in range(len(res)):
            if res[z] in res[z+1:]:
                continue
            else:
                new_res.append(res[z])

        return new_res




nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0]
x = Solution()

print(x.threeSum(nums))