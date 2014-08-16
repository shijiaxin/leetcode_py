class Solution:
	# @param s, a string
	# @return an integer
	def lengthOfLastWord(self, s):
		n=len(s);
		if n ==0 :
			return 0;
		size=0;
		while(n>0):
			if(s[n-1]==" "):
				n-=1;
			else:
				break;
		while(n>0):
			if(s[n-1]!=" "):
				size+=1;
				n-=1;
			else:
				break;
		return size;
s=Solution();
print s.lengthOfLastWord("");
print s.lengthOfLastWord("a ");
print s.lengthOfLastWord("Hello World");
