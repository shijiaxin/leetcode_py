class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		ht={};
		order=1;
		for i in num:
			if((target-i) in ht):
				return (ht[target-i],order);
			ht[i]=order;
			order+=1;


