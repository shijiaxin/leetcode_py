class Solution:
	# @param A a list of integers
	# @return nothing, sort in place
	def sortColors(self, A):
		zero=0;
		one=0;
		pos=0;
		while(pos<len(A)):
			if(A[pos]==0):
				zero+=1;
			if(A[pos]==1):
				one+=1;
			pos+=1;
		pos=0;
		while(pos<len(A)):
			if(zero>0):
				A[pos]=0;
				zero-=1;
			elif(one>0):
				A[pos]=1;
				one-=1;
			else:
				A[pos]=2;
			pos+=1;
s=Solution();
A=[1,2,0,0,2,1,1,2,0];
s.sortColors(A);
print A;
