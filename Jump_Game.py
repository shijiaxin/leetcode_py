class Solution:
	# @param A, a list of integers
	# @return a boolean
	def canJump(self, A):
		if len(A)<2:
			return True;
		pos=0;
		last=pos;
		while(pos<=last):
			if(A[pos]+pos>last):
				last=A[pos]+pos;
			pos+=1;
			if(last>=len(A)-1):
				return True;
		return False;
s=Solution();
print s.canJump([2,3,1,1,4]);
print s.canJump([3,2,1,0,4]);
