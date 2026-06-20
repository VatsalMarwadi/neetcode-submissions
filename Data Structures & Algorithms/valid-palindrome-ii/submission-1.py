class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalin(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return checkPalin(left + 1, right) or checkPalin(left, right - 1)
            left += 1
            right -= 1
        return True