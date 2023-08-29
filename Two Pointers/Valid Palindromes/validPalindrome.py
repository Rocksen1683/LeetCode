class Solution:
    def isPalindrome(self, s: str) -> bool:
        sLower = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                sLower += i
        sLower = sLower.lower()
        
        forPointer = 0
        backPointer = len(sLower) - 1

        for i in range(len(sLower)//2):
            if sLower[forPointer] != sLower[backPointer]:
                return False
            else:
                forPointer+=1
                backPointer-=1
        return True
                
