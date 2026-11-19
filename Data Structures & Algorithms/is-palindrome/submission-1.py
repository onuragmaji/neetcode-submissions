class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ''.join([k.lower() for k in s if k.isalnum()])
        print(s_new)
        return s_new==s_new[::-1]