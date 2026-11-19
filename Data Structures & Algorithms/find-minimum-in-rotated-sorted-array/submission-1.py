class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        min_num = float('inf')
        while i<=j:
              mid = (i+j)//2
              min_num = min(min_num,nums[mid])
              if nums[mid]>nums[j]:
                 i=mid+1
              else:
                 j=mid-1

        return min_num              
        