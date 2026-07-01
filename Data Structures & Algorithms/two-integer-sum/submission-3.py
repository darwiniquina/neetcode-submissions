class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        items = {}

        for index, value in enumerate(nums):

            needed = target - value

            print("NEEDED", needed, "ITEMS", items)      

            if needed in items:
                return [items[needed], index]
            else:
                items[value] = index