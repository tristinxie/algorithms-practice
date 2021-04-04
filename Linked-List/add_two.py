"""
You are given two non-empty linked lists representing two non-negative integers. The digits are 
stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        l1_iter = l1
        l2_iter = l2
        carry = 0
        output = ListNode()
        output_iter = output
        while l1_iter or l2_iter != None:
            if l1_iter:
                num1 += str(l1_iter.val)
                l1_iter = l1_iter.next
            else:
                num1 += "0"
            if l2_iter:
                num2 += str(l2_iter.val)
                l2_iter = l2_iter.next
            else:
                num2 += "0"
        max_length = max(len(num1), len(num2)) 
        for i in range(max_length):
            result = int(num1[i]) + int(num2[i]) + carry
            if result < 10:
                output_iter.val = result
                carry = 0
            else:
                output_iter.val = result % 10
                carry = 1
            if carry and i == max_length - 1:
                output_iter.next = ListNode(1)
            elif i < max_length - 1:
                output_iter.next = ListNode(0)
            output_iter = output_iter.next
        return output