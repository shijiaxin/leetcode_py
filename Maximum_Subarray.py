class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
		if(A==[]):
			return 0;
		ssum=0;
		mmax=A[0];
		pos=0;
		while(pos<len(A)):
			ssum=ssum+A[pos];
			if(ssum>mmax):
				mmax=ssum;
			if(ssum<0):
				ssum=0;
			pos=pos+1;
		return mmax;

s=Solution();
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]);
