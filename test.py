# class Solution:
#     def __init__(self, nums, target):
#         self.nums = nums
#         self.target = target
#     def twoSum(self):
#         n = len(self.nums)
#         for j in range(n-1):
#             for i in range(j,n):
#                 if nums[j]+nums[i] == self.target:
#                     return [j,i]
# nums = [2, 7, 11, 15]
# target = 9
# t = Solution(nums, target)
# a = t.twoSum()
# print(a)
#
# class Solution:
#     def twoSum(self, nums, target):
#         n = len(nums)
#         for j in range(n-1):
#             for i in range(j,n):
#                 if nums[j]+nums[i] == target:
#                     return [j,i]
# a = [2, 7, 11, 15]
# b = 9
# c = Solution.twoSum(None,a,b)
# print(c)
#
#
# def twoSum(self, nums, target):
#     # Create a num to index dictionary
#     index_map = {}
#
#     for i in xrange(len(nums)):
#         if nums[i] in index_map:
#             return [index_map[nums[i]], i]
#
#         # create entry
#         index_map[target - nums[i]] = i

