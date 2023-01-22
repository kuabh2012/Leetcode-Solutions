from typing import *
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using sorting o(nlogn)
        
        nums.sort()
        longest = 0
        curr_longest = min(1 , len(nums))
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i]  == nums[i-1]+1:
                curr_longest +=1
            else:
                longest = max(longest , curr_longest)
                curr_longest = 1
        return max(longest , curr_longest)

# using Hasset
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        
        for num in nums_set:
            if num -1 not in nums_set:
                current_length =1
                current_num = num
                while current_num +1 in nums_set:
                    current_num +=1
                    current_length +=1
                longest = max(longest , current_length)
        return longest
        
nums = [100,4,200,1,3,2]      
        