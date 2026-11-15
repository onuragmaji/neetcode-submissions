class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookup = dict()

        for i,num in enumerate(nums):
            if target-num in lookup.keys():
               return [lookup[target-num],i]
            else:
                lookup[num] = i
        return []

