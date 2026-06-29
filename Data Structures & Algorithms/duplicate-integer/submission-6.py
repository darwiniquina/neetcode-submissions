class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = {}
        
        for item in nums:
            if item not in exists:
                exists[item] = True
            else:
                return True

        return False