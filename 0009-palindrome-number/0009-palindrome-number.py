class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        elif x != 0 and x % 10 ==0:
            return False
        s = str(x)
        return s == s[::-1]
        