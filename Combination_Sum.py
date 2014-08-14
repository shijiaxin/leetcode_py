class Solution:
	def helper(self, candidates, target):
		if len(candidates)==0:
			return []; 
		if len(candidates)==1:
			if target%candidates[0]==0:
				return [candidates*(target/candidates[0])];
			return [];
		last=candidates[-1];
		result=[];
		if(target%last==0):
			result=[([last]*(target/last))];
		n_last=0;
		while(target-n_last*last>0):
			answer=self.helper(candidates[:-1],target-n_last*last);
			for e in answer:
				result.append(e+[last]*n_last);
			n_last+=1;
		return result;
	# @param candidates, a list of integers
	# @param target, integer
	# @return a list of lists of integers
	def combinationSum(self, candidates, target):
		candidates.sort();
		return self.helper(candidates,target);
s=Solution();
print s.combinationSum([2,3,6,7],7);		
print s.combinationSum([8,7,4,3],11);		
