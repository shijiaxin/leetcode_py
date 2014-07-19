class Solution:	
	# @param A  a list of integers
	# @param m  an integer, length of A
	# @param B  a list of integers
	# @param n  an integer, length of B
	# @return nothing
	def merge(self, A, m, B, n):
		pos=n+m;
		while(n>0 and m>0):
			if(B[n-1]>A[m-1]):
				A[pos-1]=B[n-1];
				n-=1;
			else:
				A[pos-1]=A[m-1];
				m-=1;
			pos-=1;
		while(n>0):
			A[n-1]=B[n-1];
			n-=1;
s=Solution();
A=[1,3,5,9,0,0,0];
s.merge(A,4,[2,6,10],3);
print A;
