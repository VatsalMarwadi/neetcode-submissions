class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Bubble Sort
        # n = len(nums)
        # for i in range(n - 1):
        #     swap = False
        #     for j in range(n - 1 -i):
        #         if nums[j] > nums[j + 1]:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             swap = True
        #     if not swap:
        #         break
        # return nums

        n = len(nums)
        for i in range(n - 1):
            mid = i
            for j in range(i + 1, n):
                if nums[j] < nums[mid]:
                    mid = j
            if mid != i:
                nums[i], nums[mid] = nums[mid], nums[i]
        return nums