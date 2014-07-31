class Solution:
		# if we have a array like 
		# 4 5 6 7 3 9 8 2 1
		# we need to swap 3 and 8,
		# then reverse the 9 3 2 1
	def find_next(self,prev):
		n=len(prev);
		result=prev[:];
		pos=n-2;
		while(pos>=0):
			if(prev[pos]>prev[pos+1]):
				pos-=1;
			else:
				# pos now point to the first place to swap
				second=n-1;
				while(prev[second]<prev[pos]):
					second-=1;
				result[pos]=prev[second];
				result[second]=prev[pos];
				end=n-1;
				pos+=1;
				while(pos<end):
					result[pos],result[end]=result[end],result[pos];
					end-=1;
					pos+=1;
				return result;
		# this is the last one;
		return [];
	# @param num, a list of integer
	# @return a list of lists of integers
	def permute(self, num):
		current=num[:];
		current.sort();
		result=[];
		while(current!=[]):
			result+=[current];
			current=self.find_next(current);
		return result;
s=Solution();
print s.permute([1,2,3]);
