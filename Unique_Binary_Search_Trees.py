class Solution:
    def __init__(self):
        self.result= [1,1,2];
    # @return an integer
    def numTrees(self, n):
        if(len(self.result)<= n+1):
            self.result+= [-1]*(n+1-len(self.result));
        if(self.result[n]>0):
            return self.result[n];
        answer=0;
        for i in range(0,n):
            answer+=self.numTrees(i)*self.numTrees(n-1-i);
        self.result[n]=answer;
        return answer;

s=Solution();
print s.numTrees(3);
print s.numTrees(4);
print s.numTrees(5);
print s.numTrees(10);