class Solution:
	# @param triangle, a list of lists of integers
	# @return an integer
	def minimumTotal(self, triangle):
		l=len(triangle);
		if l==0:
			return 0;
		s=triangle[l-1][:];
		while(l>1):
			for pos in range(l-1):
				s[pos]=min(s[pos],s[pos+1])+triangle[l-2][pos];
			l-=1;
		return s[0];
triangle=[[2],[3,4],[6,5,7],[4,1,8,3]];
s=Solution();
print s.minimumTotal(triangle);

