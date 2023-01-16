class Solution:
    def isPalindrome(self, s: str) -> bool:
        sAlpha = ""
        for char in s:
            if (char.isalpha() or char.isdigit()):
                sAlpha += char
        sLower = sAlpha.lower()
        length = len(sLower)
        sForward = ""
        sBack = ""
        forPointer = 0
        backPointer = length - 1

        for i in range(length//2):
            sForward += sLower[forPointer]
            sBack += sLower[backPointer]
            forPointer += 1
            backPointer -= 1
        if sForward == sBack:
            return True
        else:
            return False
