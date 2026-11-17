class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, i_num in enumerate(nums):
            for j, j_num in enumerate(nums):
                if i_num + j_num == target and i != j:
                    return [i, j]