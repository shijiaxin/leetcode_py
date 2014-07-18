class Solution:
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		if(len(s1)+len(s2) !=len(s3)):
			return False;
		arr=[[]]*(1+len(s1));
		for i in range (1+len(s1)):
			arr[i]=[0]*(1+len(s2));
		arr[0][0]=1;
		pos=1;
		while(pos<=len(s1)):
			if(s1[pos-1]==s3[pos-1]):
				arr[pos][0]=1;
			else:
				break;
			pos+=1;
		pos=1;
		while(pos<=len(s2)):
			if(s2[pos-1]==s3[pos-1]):
				arr[0][pos]=1;
			else:
				break;
			pos+=1;
		for i in range(1,len(s1)+1):
			for j in range(1,len(s2)+1):
				if s1[i-1]==s3[i+j-1] and arr[i-1][j]==1 :
					arr[i][j]=1;
				if s2[j-1]==s3[i+j-1] and arr[i][j-1]==1 :
					arr[i][j]=1;
		return arr[len(s1)][len(s2)]==1;
s=Solution();
print s.isInterleave("a","","c");
print s.isInterleave("aabd","abdc","aabdabcd");
print s.isInterleave("aabcc","dbbca","aadbbcbcac");
print s.isInterleave("aabcc","dbbca","aadbbbaccc");
