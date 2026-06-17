class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        w1 = 0
        w2 = 0
        res = []
        while w1 < len(word1) or w2 < len(word2):
            if i % 2 == 0:
                if w1 < len(word1):
                    res.append(word1[w1])
                    w1 += 1
            else:
                if w2 < len(word2):
                    res.append(word2[w2])
                    w2 += 1
            i += 1
        return "".join(res)