class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low_index = 0
        high_index = len(nums)-1

        while low_index <= high_index:
            middle_index = (high_index + low_index) // 2
            if nums[middle_index] == target:
                return middle_index
            elif nums[middle_index] < target:
                low_index = middle_index + 1
            elif nums[middle_index] > target:
                high_index = middle_index - 1

        return -1