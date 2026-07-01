class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        exists = {}

        for item in nums:
            if item in exists:
                return True
            else:
                exists[item] = True

        return False