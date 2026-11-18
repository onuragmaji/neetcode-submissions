class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  

        l = 0
        r = 0
        max_count = 0
        look_up = set()
        for r in range(len(s)):
            while s[r] in look_up:
                  look_up.remove(s[l])
                  l+=1
            look_up.add(s[r])
            max_count = max(max_count,len(look_up))

        return max_count    






                   
                     
              


             
        
        