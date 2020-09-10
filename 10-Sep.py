"""
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
e.g. nums = [1, 2, 4, 6, 7] target = 13, return [3, 4]
e.g. nums = [1, 1] target = 6 return [0,1]
"""
def twoSum(nums: List[int], target: int) -> List[int]:
    h = {}
    for loc, num in enumerate(nums):
    remaining = target - num
    if remaining not in h:
       h[num] = loc
    else:
       return [h[n], loc]
       
