class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        result = []
        max_freq = max(freq.values())
        for f in range(max_freq, 0, -1):
            for num in freq:
                if freq[num] == f:
                    result.append(num)
                    if len(result) == k:
                        return result