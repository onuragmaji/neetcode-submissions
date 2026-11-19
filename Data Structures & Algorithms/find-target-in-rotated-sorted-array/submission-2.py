class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        min_val = float('inf')
        min_loc = -1

        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                 return mid
            if nums[mid]<min_val:
               min_val = nums[mid] 
               min_loc = mid
               print(min_val,min_loc)
            if nums[mid]>nums[j]:
               i=mid+1
            else:
               j=mid-1 
        if min_loc ==0:
           l=0
           r=len(nums)-1
           print("I am here")

        elif target>=nums[0] and target<=nums[min_loc-1]:
           l=0
           r=min_loc-1
        else:
           l=min_loc
           r=len(nums)-1
        print(l,r)
        while l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                   return mid
                if nums[mid]<target:
                   l=mid+1
                else:
                   r=mid-1                    

        print(min_val,min_loc)   
        return -1    

             
              