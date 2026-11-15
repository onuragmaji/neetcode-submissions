class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
           return False

        aux_list1 = [0]*256
        aux_list2 = [0]*256

        for i in range(len(s)):
            aux_list1[ord(s[i])] += 1
            aux_list2[ord(t[i])] += 1
        return aux_list1==aux_list2   
