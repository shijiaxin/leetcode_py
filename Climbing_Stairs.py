class Solution:
	# @param n, an integer
	# @return an integer
	def climbStairs(self, n):
		if(n<3):
			return n;
		a=1;
		b=2;
		for i in range(n-2):
			a,b=b,a+b;
		return b;

s=Solution();
print s.climbStairs(3);
print s.climbStairs(4);
print s.climbStairs(5);
