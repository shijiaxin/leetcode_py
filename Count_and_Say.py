class Solution:
	def get_next(self,s):
		n=len(s);
		pos=0;
		num=0;
		result="";
		while(True):
			num+=1;
			if pos<n-1 and s[pos]== s[pos+1]:
				pos+=1;
			else:
				result+=str(num)+s[pos];
				num=0;
				pos+=1;
			if(pos>=n):
				break;
		return result;
	# @return a string
	def countAndSay(self, n):
		s="1";
		while(n>1):
			s=self.get_next(s);
			n-=1;
		return s;
s=Solution();
print s.countAndSay(1);
print s.countAndSay(2);
print s.countAndSay(3);
print s.countAndSay(4);
