class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        count = 1

        while True:
            if count in nums:
                count += 1
                continue
            return count


        # for num in nums:
        #     if num >= smallest:
        #         smallest = num