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

"""

每次按照“位置”和“数值”来遍历这个list，如果遍历的数据不在已遍历的字典中，将这个遍历的数据存入字典，
以key = 数值， value = “位置”的方式存入。
每次循环用target减去这个循环的数值，得到remaining，查询remaining是否存在于遍历过的字典中，如果存在，
就意味着我们已经找到了可以相加得到target的两位数， 返回key = remaining对应的value以及此时的location。

"""

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

e.g.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
def addTwoNumbers(self, l1: ListNode, l2: ListNode, c = 0) -> ListNode:
    val = l1.val + l2.val + c
    c = val // 10
    ret = ListNode(val % 10 ) 
        
    if (l1.next != None or l2.next != None or c != 0):
        if l1.next == None:
            l1.next = ListNode(0)
        if l2.next == None:
            l2.next = ListNode(0)
        ret.next = self.addTwoNumbers(l1.next,l2.next,c)
    return ret    

"""
Given a string s, find the length of the longest substring without repeating characters.

e.g.
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
def lengthOfLongestSubstring(self, s: str) -> int:
    dic = {}
    max_so_far = curr_max = start = 0
        
    for index, i in enumerate(s):
        if i in dic and dic[i] >= start:
            max_so_far = max(max_so_far, curr_max)
            curr_max = index - dic[i]
            start = dic[i] + 1
                
        else:
            curr_max += 1
                
        dic[i] = index
        
    return max(max_so_far, curr_max)


"""

"""
