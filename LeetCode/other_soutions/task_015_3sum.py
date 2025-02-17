class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Перевірка обмежень
        if not (3 <= len(nums) <= 3000):
            raise ValueError("The length of nums must be between 3 and 3000.")
        if not all(-10**5 <= num <= 10**5 for num in nums):
            raise ValueError("Each element in nums must be between -10^5 and 10^5.")

        nums.sort()  # Сортуємо список для ефективного пошуку
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Пропускаємо дублікати
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1  # Збільшуємо лівий індекс
                elif total > 0:
                    right -= 1  # Зменшуємо правий індекс
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:  # Пропускаємо дублікати
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:  # Пропускаємо дублікати
                        right -= 1

        return res
