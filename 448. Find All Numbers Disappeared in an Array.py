# 448. Find All Numbers Disappeared in an Array
# Easy
# 4470312Add to ListShare
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
 
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
# Input: nums = [1,1]
# Output: [2]
 
# Constraints:
# •	n == nums.length
# •	1 <= n <= 105
# •	1 <= nums[i] <= n
 
# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

# S1
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        num = set(nums)
        for i in range(1, len(nums)+1):
            if i not in num:
                res.append(i)
        return res

# S2:
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        num = collections.Counter(nums)
        for i in range(1, len(nums)+1):
            if i not in num:
                res.append(i)
        return res
            
#  S3

# 原地变负来标记。比如对于[4, 3, 2, 7, 8, 2, 3, 1]，把这些元素作为list的索引，指向的元素变换成负数，那么，没有变换成负数的位置就是没有人指向它，故这个位置对应的下标没有出现。


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            idx = (abs(nums[i]))-1
            if nums[idx] > 0:
                nums[idx] *= -1
        for i in range(1, len(nums)+1):
            if nums[i-1] >0:
                res.append(i)
        return res
            
