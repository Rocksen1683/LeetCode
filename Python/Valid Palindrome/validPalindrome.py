class Solution:
    def isPalindrome(self, s: str) -> bool:
        sAlpha = ""
        for char in s:
            if (char.isalpha() or char.isdigit()):
                sAlpha += char
        sLower = sAlpha.lower()
        sReverse = sLower[::-1]

        if sLower == sReverse:
            return True
        else:
            return False
