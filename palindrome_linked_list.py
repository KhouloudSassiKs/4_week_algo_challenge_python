# Definition for linked list 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val        # Value of the current node
        self.next = next      # Pointer to the next node in the list


def is_palindrome(head):
    """
    Check if a  linked list is a palindrome.
    Logic:
      1. Use slow (one_step) and fast (two_step) pointers to find the middle.
      2. Reverse the second half of the list.
      3. Compare the first half and the reversed second half node by node.
      4. Return True if all values match, otherwise False.
    """

    # an empty list or a single node is always a palindrome
    if head is None or head.next is None:
        return True

    # Step 1: Find the middle of the linked list
    one_step = head
    two_step = head
    while two_step is not None and two_step.next is not None:
        one_step = one_step.next           # move by 1
        two_step = two_step.next.next      # move by 2

    # Step 2: Reverse the second half of the list starting from the found middle
    second_half = reverse_linked_list(one_step)

    # Step 3: Compare the first half and the reversed second half
    first_half = head
    while second_half is not None:
        if first_half.val != second_half.val:
            return False                   #not a palindrome
        first_half = first_half.next
        second_half = second_half.next

    # If we reach here, all nodes matched
    return True


def reverse_linked_list(head):
    """
    Reverse a linked list in-place.
    Returns the new head of the reversed list.
    """
    prev = None
    current = head

    while current:
        next_node = current.next   # store next node
        current.next = prev        # reverse current node’s pointer
        prev = current             # move prev forward
        current = next_node        # move current forward

    return prev  # new head of reversed list
