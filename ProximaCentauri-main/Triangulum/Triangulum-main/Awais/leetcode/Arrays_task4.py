'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
        
        
            if nums[i] == target:
                return i
            
        
            elif nums[i] > target:
                return i
        return len(nums)