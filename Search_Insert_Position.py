class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        if(A==[]):
            return 0;
        res=0;
        for i in A:
            if(i>=target):
                return res;
            res+=1;
        return len(A);

s=Solution();
print s.searchInsert([1,3,5,6], 5);
print s.searchInsert([1,3,5,6], 2);
print s.searchInsert([1,3,5,6], 7);
print s.searchInsert([1,3,5,6], 0);
