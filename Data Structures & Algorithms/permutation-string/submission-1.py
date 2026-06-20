class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        windowCount = [0] * 26
        for ch in s1:
            s1Count[ord(ch) - ord('a')] += 1
        windowSize = len(s1)
        for i in range(windowSize):
            windowCount[ord(s2[i]) - ord('a')] += 1
        if s1Count == windowCount:
            return True
        for i in range(windowSize, len(s2)):
            windowCount[ord(s2[i]) - ord('a')] += 1
            windowCount[ord(s2[i - windowSize]) - ord('a')] -= 1
            if s1Count == windowCount:
                return True
        return False
            