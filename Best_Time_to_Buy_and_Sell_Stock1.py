class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if len(prices) <=1 :
			return 0;
		benefits=[0]*(len(prices)-1);
		i=0;
		while(i<len(benefits)):
			benefits[i]=prices[i+1]-prices[i];
			i+=1;
		pos=0;
		max_sum=0;
		cur_sum=0;
		while(pos<len(benefits)):
			cur_sum+=benefits[pos];
			if(cur_sum>max_sum):
				max_sum=cur_sum;
			if(cur_sum<0):
				cur_sum=0;
			pos+=1;
		return max_sum;
s=Solution();
print s.maxProfit([1,2,3,4,5,6,7,8,7,6,5,4,9]);
