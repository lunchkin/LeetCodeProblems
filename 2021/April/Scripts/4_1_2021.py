# Problem: Given the head of a singly linked list, return true if it is a palindrome.

# Link: https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3693/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        myList = []

        # While the head still has a value we are in the list
        while head is not None:
            myList.append(head.val)
            head = head.next

        # Return if the list is the same backwards as it is forwards
        return myList == myList[::-1]
