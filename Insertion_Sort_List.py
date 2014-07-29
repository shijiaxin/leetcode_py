import COMMON
class Solution:
	# @param head, a ListNode
	# @return a ListNode
	def insertionSortList(self, head):
		if(head==None):
			return None;
		result=head;
		head=head.next;
		result.next=None;
		while(head!=None):
			current=head;
			head=head.next;
			current.next=None;
			if(current.val<result.val):
				current.next=result;
				result=current;
			else:
				pointer=result;
				while(pointer.next!=None and pointer.next.val<current.val):
					pointer=pointer.next;
				current.next=pointer.next;
				pointer.next=current;
		return result;
s=Solution();
COMMON.print_list(s.insertionSortList(COMMON.build_list([1,5,2,4,3])));
