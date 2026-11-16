class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        results = list()
        nums_sorted = sorted(nums)
        for start in range(len(nums_sorted)):
            i = start+1
            j=len(nums_sorted)-1
            while i<j:
                val = nums_sorted[start]+nums_sorted[i]+nums_sorted[j]
                if val == 0:
                    res = [nums_sorted[start],nums_sorted[i],nums_sorted[j]]
                    if res not in results:
                       results.append(res) 
                if val<0: 
                   i+=1
                else:
                   j-=1    

        return results    