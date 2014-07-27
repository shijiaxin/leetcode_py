class Solution:
	def __init__(self):
		self.data=[([0]*100) for i in range(100)];
		for i in range(100):
			self.data[i][0]=1;
			self.data[0][i]=1;
	# @return an integer
	def uniquePaths(self, m, n):
		for i in range(1,m):
			for j in range(1,n):
				self.data[i][j]=self.data[i][j-1]+self.data[i-1][j];
		return self.data[m-1][n-1];
s=Solution();
print s.uniquePaths(2,2);
print s.uniquePaths(3,2);
print s.uniquePaths(3,3);
