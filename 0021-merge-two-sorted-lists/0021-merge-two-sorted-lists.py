# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        # Set the current node to the dummy node
        current = dummy
        # Traverse the two input lists simultaneously
        while list1 and list2:
            # Compare the values of the current nodes of the two lists
            if list1.val <= list2.val:
                # Append the current node of list1 to the merged list
                current.next = list1
                # Move to the next node in list1
                list1 = list1.next
            else:
                # Append the current node of list2 to the merged list
                current.next = list2
                # Move to the next node in list2
                list2 = list2.next
            # Move to the next node in the merged list
            current = current.next

        # Append any remaining nodes from list1 or list2 to the merged list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Return the head of the merged list (i.e., the next node after the dummy node)
        return dummy.next

