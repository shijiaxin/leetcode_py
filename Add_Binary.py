class Solution:
	# @param a, a string
	# @param b, a string
	# @return a string
	def addBinary(self, a, b):
		na,nb=len(a),len(b);
		if(na>nb):
			b="0"*(na-nb)+b;
		else:
			a="0"*(nb-na)+a;
		n=max(na,nb);
		result="";
		carry=0;
		for i in range(n-1,-1,-1):
			r=int(a[i])+int(b[i])+carry;
			if r>1:
				carry=1;
				result=str(r-2)+result;
			else:
				carry=0;
				result=str(r)+result;
		if(carry>0):
			result="1"+result;
		return result;
s=Solution();
print s.addBinary("11","1");
