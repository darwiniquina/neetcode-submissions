class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        exists = {}
        for i in nums:
            if i in exists:
                return True
            
            exists[i] = True

        return False
        