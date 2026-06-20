class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        l1 = 0
        l2 = 0
        res = ""
        while l1 < len(word1) or l2 < len(word2):
            if i % 2 == 0:
                if l1 < len(word1):
                    res += word1[l1]
                    l1 += 1
            else:
                if l2 < len(word2):
                    res += word2[l2]
                    l2 += 1
            i += 1
        return res