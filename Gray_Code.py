class Solution:
	# @return a list of integers
	def grayCode(self, n):
		if(n<=0):
			return [0];
		if(n==1):
			return [0,1];
		r= self.grayCode(n-1);
		oldsize=len(r);
		r=r+[0]*oldsize;
		pos=0;
		while(pos<oldsize):
			r[oldsize+pos]=oldsize+r[oldsize-1-pos];
			pos+=1;
		return r;
s=Solution();
print s.grayCode(4);
