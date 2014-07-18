class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		if(len(ratings)<2):
			return len(ratings);
		length=len(ratings);
		result=[1]*length;
		pos=1;
		while(pos<length):
			if(ratings[pos]>ratings[pos-1]):
				result[pos]=result[pos-1]+1;
				pos+=1;
				continue;
			if(ratings[pos]==ratings[pos-1]):
				pos+=1;
				continue;
			p=pos-1;
			while(p>=0):
				if(ratings[p]>ratings[p+1] and result[p]==result[p+1]):
					result[p]=result[p+1]+1;
					p-=1;
				else:
					break;
			pos+=1;
		return sum(result);

s=Solution();
print s.candy([1,2,3,4,3,2,3,4,5,2,3,3,3,1,5,2]);
