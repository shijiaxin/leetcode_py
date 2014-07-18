class Solution:
	# @param ratings, a list of integer
	# @return an integer
	def candy(self, ratings):
		if(len(ratings)<2):
			return len(ratings);
		length=len(ratings);
		v_array=[1]*length;
		l_array=[1]*length;
		result=[(1,1)]*length;#(value,decrease length)
		pos=1;
		while(pos<length):
			if(ratings[pos]>ratings[pos-1]):
				v_array[pos]=v_array[pos-1]+1;
				pos+=1;
				continue;
			if(ratings[pos]==ratings[pos-1]):
				pos+=1;
				continue;
			prev=pos-l_array[pos];
			while(prev>=0):
				if(ratings[prev]>ratings[prev+1] and v_array[prev]==pos-prev):
					l_array[pos]+=l_array[prev];
					v_array[prev]=-1;
				else:
					break;
				prev=pos-l_array[pos];
			pos+=1;
		candy=0;
		pos=0;
		while(pos<len(result)):
			if(v_array[pos]==-1):
				pos+=1;
			else:
				m=v_array[pos];
				l=l_array[pos];
				candy+=(m+m+l-1)*l/2;
				pos+=1;
		return candy;

s=Solution();
print s.candy([2,1,2,3,5,4,3,2,1]);
#print s.candy([1,2,3,4,3,2,3,4,5,2,3,3,3,1,5,2]);
