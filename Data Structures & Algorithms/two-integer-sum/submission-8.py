class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for index, num in enumerate(nums):
            for i_index, i_num in enumerate(nums):

                if index == i_index:
                    continue

                if num + i_num == target:
                    return [index, i_index]

        return [0,0]

                
                