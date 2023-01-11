# Sorting solution for Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = sorted(s)
        b = sorted(t)

        aString = "".join(a)
        bString = "".join(b)

        if aString == bString:
            return True
        else:
            return False