from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        look_up = defaultdict(list)

        for i in strs:
            key = ''.join(sorted(i))
            look_up[key].append(i)
        return [val for _,val in look_up.items()]

          
                     
