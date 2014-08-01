class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of lists of integers
	def rotate(self, matrix):
		n=len(matrix);
		# (0,0)->(0,n-1)->(n-1,n-1)->(n-1,0)
		# (i,j)->(j,n-1-i)->(n-1-i,n-1-j)->(n-1-j,i)
		h=n/2;
		w=(n+1)/2;
		for i in range(h):
			for j in range(w):
				tmp=matrix[i][j];
				matrix[i][j]=matrix[n-1-j][i];
				matrix[n-1-j][i]=matrix[n-1-i][n-1-j];
				matrix[n-1-i][n-1-j]=matrix[j][n-1-i];
				matrix[j][n-1-i]=tmp;
		return matrix;
