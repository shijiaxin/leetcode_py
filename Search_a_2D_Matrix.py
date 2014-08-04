class Solution:
	# @param matrix, a list of lists of integers
	# @param target, an integer
	# @return a boolean
	def searchMatrix(self, matrix, target):
		m=len(matrix);
		if(m==0):
			return False;
		n=len(matrix[0]);
		if(n==0):
			return False;
		if(matrix[0][0]>target or matrix[m-1][n-1]<target):
			return False;
		if(matrix[0][0]==target or matrix[m-1][n-1]==target):
			return True;
		begin=0;
		end=n*m-1;
		while(True):
			middle=begin+(end-begin)/2;
			if(middle==begin or middle==end):
				return False;
			if(matrix[middle/n][middle%n]==target):
				return True;
			if(matrix[middle/n][middle%n]<target):
				begin=middle;
			else:
				end=middle;
s=Solution();
print s.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],4);
			
		
