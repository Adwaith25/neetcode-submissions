class Solution:
    def isPalindrome(self, s: str) -> bool:
        a1=(s.replace(" ","")).lower()
        a=""
        for i in a1:
            if(i.isalnum()):
                a+=i
        
        if(a[::-1]==a):
            return True
        else:
            return False
        