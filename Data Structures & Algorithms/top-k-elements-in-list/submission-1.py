class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        res = []
        maxFreq = max(freq.values())
        for f in range(maxFreq, 0, -1):
            for num in freq:
                if freq[num] == f:
                    res.append(num)
                    if len(res) == k:
                        return res