class Solution:
	# @param x, a float
	# @param n, a integer
	# @return a float
	def pow(self, x, n):
		if(n==0):
			return 1;
		if(n<0):
			return 1/self.pow(x,-1*n);
		r=1;
		for i in range(63,-1,-1):
			r=r**2;
			if((n>>i) % 2 ==1):
				r*=x;
		return r;
s=Solution();
print s.pow(2,3);	
