class Solution:
	# @param matrix, a list of lists of integers
	# @return a list of integers
	def spiralOrder(self, matrix):
		m=len(matrix);
		if m==0:
			return [];
		n=len(matrix[0]);
		if n==0:
			return [];
		round=0;
		result=[];
		while(True):
			if(m-2*round <=0 or n-2*round <=0 ):
				break;
			if(m-2*round ==1):
				for j in range(round,n-round):
					result.append(matrix[round][j]);
				break;
			if(n-2*round ==1):
				for i in range(round,m-round):
					result.append(matrix[i][round]);
				break;
			for j in range(round,n-round):
				result.append(matrix[round][j]);
			for i in range(round+1,m-round-1):
				result.append(matrix[i][n-round-1]);
			for j in range(round,n-round):
				result.append(matrix[m-round-1][n-1-j]);
			for i in range(round+1,m-round-1):
				result.append(matrix[m-1-i][round]);
			round+=1;
		return result;
s=Solution();
print s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]);
			
