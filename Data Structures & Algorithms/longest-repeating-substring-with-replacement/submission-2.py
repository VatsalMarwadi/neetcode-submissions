class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            freq = [0] * 26
            maxFreq = 0
            for j in range(i, len(s)):
                index = ord(s[j]) - ord('A')
                freq[index] += 1
                maxFreq = max(maxFreq, freq[index])
                windowSize = j - i + 1
                if windowSize - maxFreq <= k:
                    res = max(res, windowSize)
        return res                