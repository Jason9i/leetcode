# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        cur_node = head
        pre_node = None

        while cur_node != None:
            # locate next one
            next_node = cur_node.next
            # reverse cur_node and pre_node
            cur_node.next = pre_node
            pre_node = cur_node
            #iterate to next one and loop
            cur_node = next_node

        return pre_node

