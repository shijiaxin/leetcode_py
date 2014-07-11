class Solution:
	def check_valid(self,arr,n,k):
		if(k==0):
			return True;
		for i in range(k):
			diff=arr[i]-arr[k];
			if((diff == 0) or (diff == i-k) or (diff== k-i)):
				return False;
		return True;
	# @return an integer
	def totalNQueens(self, n):
		if(n==1):
			return 1;
		if(n<4):
			return 0;
		total=0;
		Queens=[-1]*n;
		k=0;
		while(k>=0):
			Queens[k]+=1;
			if(Queens[k]==n):
				Queens[k]=-1;
				k-=1;
				continue;
			ans=self.check_valid(Queens,n,k);
			if(ans and (k==n-1)):
				total+=1;
				Queens[k]=-1;
				k-=1;
				continue;
			if(ans):
				k+=1;
				continue;
		return total;
s=Solution();
print s.totalNQueens(4);
print s.totalNQueens(10);			
