class Solution:
	# @param digits, a list of integer digits
	# @return a list of integer digits
	def plusOne(self, digits):
		if(digits==[]):
			return ;
		carry=1;
		pos=len(digits)-1;
		while(pos>=0):
			digits[pos]+=carry;
			carry=0;
			if(digits[pos]==10):
				digits[pos]=0;
				carry=1;
			else:
				break;
			pos-=1;
		if(carry==1):
			return [1]+digits;
		else:
			return digits;
s=Solution();
print s.plusOne([9,9,9]);
print s.plusOne([9,7,9]);
