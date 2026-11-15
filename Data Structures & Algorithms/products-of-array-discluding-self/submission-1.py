class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = 1
        end = 1
        l1 = [1]*len(nums)
        l2 = [1]*len(nums)
        for i in range(1,len(l1)):
            l1[i] = l1[i-1]*nums[i-1]
        
        for j in range(len(l2)-2,-1,-1):
            l2[j] = l2[j+1]*nums[j+1] 

        result = [1]*len(nums)
        for i in range(len(l1)):
            result[i]=l1[i]*l2[i]

        return result    




