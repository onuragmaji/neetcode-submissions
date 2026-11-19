class Solution:
    def isValid(self, s: str) -> bool:
        val = {")":"(","}":"{","]":"["}
        lookup = list()
        for i in s:
            if i in val.values():
               lookup.append(i)
            else:
                if len(lookup)!=0:
                    v = lookup.pop()
                    if v != val[i]:
                        return False
                else:
                    return False          
        return len(lookup)==0       
                     
                  