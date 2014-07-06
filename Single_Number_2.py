class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        d={};
        for i in A:
            if(i in d):
                d[i]+=1;
            else:
                d[i]=1;
        for i in d:
            if(d[i]==1):
                return i;

s=Solution();
print s.singleNumber([1,1,1,3,3,3,4]);
print s.singleNumber([1]);