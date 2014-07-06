class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
		r=0;
		for i in A:
			r=r^i;
		return r;	
s= Solution();
print s.singleNumber([2,2,3,4,4]);

