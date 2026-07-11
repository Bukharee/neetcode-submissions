class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority_map = {}
        n = len(nums) // 3

        for num in nums:
            if num in majority_map:
                majority_map[num] += 1
            else:
                majority_map[num] = 1
        
        answer = []
        for k,v in majority_map.items():
            if v > n:
                answer.append(k)
        return answer
        