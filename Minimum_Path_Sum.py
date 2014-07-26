class Solution:
	# @param grid, a list of lists of integers
	# @return an integer
	def minPathSum(self, grid):
		m=len(grid);
		if(m==0):
			return 0;
		n=len(grid[0]);
		if(n==0):
			return 0;
		data=[([0]*n) for i in range(m)];
		data[0][0]=grid[0][0];
		for i in range(1,m):
			data[i][0]=data[i-1][0]+grid[i][0];
		for j in range(1,n):
			data[0][j]=data[0][j-1]+grid[0][j];
		for i in range(1,m):
			for j in range(1,n):
				data[i][j]=grid[i][j]+min(data[i][j-1],data[i-1][j]);
		return data[m-1][n-1];
s=Solution();
print s.minPathSum([[1,2,3],[2,2,2],[3,2,1]]);

