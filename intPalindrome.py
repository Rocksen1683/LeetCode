class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        reverse = x[::-1]
        if x == reverse:
            return True
        return False
