class Solution:
	# @param s, a string
	# @return an integer
	def numDecodings(self, s):
		if (len(s)==0 or s[0]=="0"):
			return 0;
		if (len(s)==1):
			return 1;
		arr=[1]*(len(s)+1);
		for i in range(2,len(s)+1):
			if s[i-1]=="0":
				if (s[i-2]=="1" or s[i-2]=="2"):
					arr[i]=arr[i-2];
				else:
					return 0;
			elif(int(s[i-2:i])>26 or int(s[i-2:i])<10):
				arr[i]=arr[i-1];
			else:
				arr[i]=arr[i-2]+arr[i-1];
		return arr[len(s)];
s=Solution();
print s.numDecodings("12");
print s.numDecodings("101");
