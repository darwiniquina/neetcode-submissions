class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counted = {}

        for index, num in enumerate(nums):
            needed = target - num

            if needed in counted:
                return [counted[needed], index]

            counted[num] = index

        return [0,0]