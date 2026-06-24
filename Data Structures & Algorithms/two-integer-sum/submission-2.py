class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for key, num in enumerate(nums):
            for inner_key, inner_num in enumerate(nums):
                if (key == inner_key):
                    continue
                
                if (num + inner_num == target):
                    return [key, inner_key]
            
        return [0,0]