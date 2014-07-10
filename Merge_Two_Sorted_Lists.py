class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
class Solution:
	# @param two ListNodes
	# @return a ListNode
	def mergeTwoLists(self, l1, l2):
		if(l1==None):
			return l2;
		if(l2==None):
			return l1;
		if(l1.val<l2.val):
			r=l1;
			l1=l1.next;
		else:
			r=l2;
			l2=l2.next;
		cur=r;
		while(l1!=None and l2!=None):
			if(l1.val<l2.val):
				cur.next=l1;
				l1=l1.next;
			else:
				cur.next=l2;
				l2=l2.next;
			cur=cur.next;
		if(l1==None):
			cur.next=l2;
		else:
			cur.next=l1;
		return r;
a1=ListNode(1);
a2=ListNode(2);
a3=ListNode(3);
a4=ListNode(4);
a5=ListNode(5);
a1.next=a4;
a2.next=a3;
a3.next=a5;
s=Solution();
r=s.mergeTwoLists(a1,a2);
while(r!=None):
	print r.val;
	r=r.next;
