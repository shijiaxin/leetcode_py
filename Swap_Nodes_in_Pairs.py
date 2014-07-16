# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param a ListNode
	# @return a ListNode
	def swapPairs(self, head):
		if(head==None):
			return None;
		if(head.next==None):
			return head;
		tail=self.swapPairs(head.next.next);
		result=head.next;
		result.next=head;
		head.next=tail;
		return result;	    

s=Solution();
a1=ListNode(1);
a2=ListNode(2);
a3=ListNode(3);
a4=ListNode(4);
a5=ListNode(5);
a1.next=a2;
a2.next=a3;
a3.next=a4;
a4.next=a5;
r=s.swapPairs(a1);
while(r!= None):
	print r.val;
	r=r.next;
