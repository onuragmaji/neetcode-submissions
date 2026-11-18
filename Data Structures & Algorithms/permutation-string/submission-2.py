class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = [0]*256
        s2_map = [0]*256
        if len(s1)>len(s2):
           return False 

        for i in range(len(s1)):
            s1_map[ord(s1[i])]+=1
            s2_map[ord(s2[i])]+=1

        i=0
        j=len(s1)-1

        while j<len(s2):
            if s1_map == s2_map:
                return True
            s2_map[ord(s2[i])]-=1
            print(s2[i:j+1])
            i+=1    
            j+= 1
            if j <len(s2):
               s2_map[ord(s2[j])]+=1


        return False          




        





        
        