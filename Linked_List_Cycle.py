# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        first=head;
        second=head;
        while(True):
            if(second== None):
                return False;
            second = second.next;
            if(second== None):
                return False;
            if(first == second):
                return True;
            first=first.next;
            second=second.next;

a=ListNode(1);        
b=ListNode(2);        
c=ListNode(3);        
d=ListNode(4);        
e=ListNode(5);        
a.next=b;
b.next=c;
c.next=a;
d.next=e;
s=Solution();
print s.hasCycle(a);
print s.hasCycle(d);