class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest = 0
        res = set()
        for i in range(len(s)):
            while s[i] in res:
                res.remove(s[left])
                left += 1
            res.add(s[i])
            longest = max(longest, i - left + 1)
        return longest
            