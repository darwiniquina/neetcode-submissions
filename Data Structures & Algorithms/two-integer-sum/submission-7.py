class Solution:
    # loop 1
    # current founded = {}
    # index = 0, value = 3
    # needed = 7 - 3 = 4
    # The 4 in founded? NO!
    # push the current value and index to current_founded
    # current_founded = {3: 0}

    # loop 2
    # index = 1, value = 4
    # needed = (target) 7 - 4 = 3
    # Does the 3 exists in founded?
    # yes! it was made from previous loop

    # ready to exit:
    # return the index of 3 which is 0
    # then return the current index of pointer
    # answer would be [0, 1] 
    # the value of those is 3 and 4 
    # 3 + 4 = 7

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        founded = {}

        for index, value in enumerate(nums):
            needed = target - value

            if needed in founded:
                return [founded[needed], index]

            founded[value] = index

        return [0,0]