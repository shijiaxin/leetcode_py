class Solution:
	# @param a list of integers
	# @return an integer
	def removeDuplicates(self, A):
		if(A==[]):
			return 0;
		last=A[0];
		length=1;
		pos=1;
		while(pos<len(A)):
			if(A[pos]!=last):
				A[length]=A[pos];
				last=A[length];
				length+=1;
			pos+=1;
		return length;

s=Solution();
A=[1,1,2,3,4,7,7,7,8];
print s.removeDuplicates(A);
print A;

