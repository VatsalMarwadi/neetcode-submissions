class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        for i in range(len(s)):
            freq = [0] * 26
            max_freq = 0
            for j in range(i, len(s)):
                index = ord(s[j]) - ord('A')
                freq[index] += 1
                max_freq = max(max_freq, freq[index])
                window_size = j - i + 1
                if window_size - max_freq <= k:
                    result = max(result, window_size)
        return result