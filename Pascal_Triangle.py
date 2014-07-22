class Solution:
	# @return a list of lists of integers
	def generate(self, numRows):
		if (numRows==0):
			return [];
		if (numRows==1):
			return [[1]];
		result=self.generate(numRows-1);
		next=[1]*numRows;
		i=1;
		while(i<numRows-1):
			next[i]=result[numRows-2][i-1]+result[numRows-2][i];
			i+=1;
		result+=[next];
		return result;

s=Solution();
print s.generate(5);
