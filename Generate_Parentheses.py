class Solution:	
	def __init__(self):
		self.data=[[""],["()"],["()()","(())"]];
	# @param an integer
	# @return a list of string
	def generateParenthesis(self, n):
		if(n<len(self.data)):
			return self.data[n];
		result=[];
		for i in range(n):
			for inside in self.generateParenthesis(i):
				for outside in self.generateParenthesis(n-1-i):
					str="("+inside+")"+outside;
					result+=[str];
		self.data+=[result];
		return result;
s=Solution();
print s.generateParenthesis(1);
print s.generateParenthesis(2);
print s.generateParenthesis(3);
print s.generateParenthesis(4);
