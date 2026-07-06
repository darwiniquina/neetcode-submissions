class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        founded = {}

        for index, value in enumerate(nums):
            # 7 - 3 = 4
            needed = target - value

            if needed in founded:
                return [founded[needed], index]

            founded[value] = index

        return [0,0]