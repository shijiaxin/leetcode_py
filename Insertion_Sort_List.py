import COMMON
class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def insertionSortList(self, head):
		if(head==None):
			return None;
		result=head;
		p1=head;
		while(True):
			# from start to p1 ,it's a sorted List
			p2=p1.next;
			if(p2==None):
				break;
			if(p2.val>=p1.val):
				p1=p2;
				continue;
			# insert p2 to the old list
			p1.next=p2.next;
			if(p2.val<result.val):
				p2.next=result;
				result=p2;
			else:
				pointer=result;
				while(pointer.next.val<p2.val):
					pointer=pointer.next;
				p2.next=pointer.next;
				pointer.next=p2;
		return result;
s=Solution();
COMMON.print_list(s.insertionSortList(COMMON.build_list([1,5,2,4,3])));
