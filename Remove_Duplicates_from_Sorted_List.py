# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if(head==None):
            return head;
        current=head;
        while(current!=None):
            if(current.next==None):
                return head;
            if(current.next.val == current.val):
                current.next=current.next.next;
            else:
                current=current.next;
        return head;
s=Solution();

a=ListNode(1);
b=ListNode(1);
c=ListNode(2);
a.next=b;
b.next=c;

current=s.deleteDuplicates(a);
while(current!=None):
    print current.val;
    current=current.next;
##########
a=ListNode(1);
b=ListNode(1);
c=ListNode(2);
d=ListNode(3);
e=ListNode(3);
a.next=b;
b.next=c;
c.next=d;
d.next=e;
current=s.deleteDuplicates(a);
while(current!=None):
    print current.val;
    current=current.next;
#########
a=ListNode(1);
b=ListNode(1);
c=ListNode(1);
a.next=b;
b.next=c;
current=s.deleteDuplicates(a);
while(current!=None):
    print current.val;
    current=current.next;

