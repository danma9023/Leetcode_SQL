# 234. Palindrome Linked List
# Easy

# 5649

# 449

# Add to List

# Share
# Given the head of a singly linked list, return true if it is a palindrome.

 

# Example 1:


# Input: head = [1,2,2,1]
# Output: true
# Example 2:


# Input: head = [1,2]
# Output: false
 

# Constraints:

# The number of nodes in the list is in the range [1, 105].
# 0 <= Node.val <= 9
 

# Follow up: Could you do it in O(n) time and O(1) space?
  
# S1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans == ans[::-1]
      
# S2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        n = len(ans)
        l, r = 0, n-1
        while l<r:
            if ans[l] != ans[r]:
                return False
            l += 1
            r -= 1
        return True
