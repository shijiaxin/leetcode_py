class Solution:
	def check(self,arr,s1,i1,s2,i2,s3):
		if(i1==len(s1) and i2==len(s2)):
			return True;
		if(arr[i1][i2]==1):
			return True;
		if(arr[i1][i2]==-1):
			return False;
		if(i1<len(s1) and s1[i1]==s3[i1+i2]):
			check1=self.check(arr,s1,i1+1,s2,i2,s3);
			if check1:
				arr[i1][i2]=1;
				return True;
		if(i2<len(s2) and s2[i2]==s3[i1+i2]):
			check2=self.check(arr,s1,i1,s2,i2+1,s3);
			if check2:
				arr[i1][i2]=1;
				return True;
		arr[i1][i2]=-1;
		return False;
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		if(len(s1)+len(s2) !=len(s3)):
			return False;
		arr=[0]*(1+len(s2));
		arr=[arr]*(1+len(s1));
		a= self.check(arr,s1,0,s2,0,s3);
		print arr;
		return a;
s=Solution();
print s.isInterleave("aabd","abdc","aabdabcd");
#print s.isInterleave("aabcc","dbbca","aadbbcbcac");
#print s.isInterleave("aabcc","dbbca","aadbbbaccc");
