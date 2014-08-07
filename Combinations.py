class Solution:
	# @return a list of lists of integers
	def combine(self, n, k):
		if k ==0 or k > n:
			return [];
		result=[];
		if k==1:
			for i in range(1,n+1):
				result.append([i]);
			return result;
		if k==n:
			element=[];
			for i in range(1,n+1):
				element.append(i);
			return [element];
		with_n   =self.combine(n-1,k-1);
		without_n=self.combine(n-1,k);
		for lst in with_n:
			result.append(lst+[n]);
		result+=without_n;
		return result;
s=Solution();
print s.combine(4,2);
