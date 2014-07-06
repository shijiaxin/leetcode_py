class Solution:
    # @return an integer
    def reverse(self, x):
        if (x>=0):
            r=x%10;
            while(x>=10):
                r*=10;
                x=x/10;
                r+=x%10;
            return r;
        return -1*(self.reverse(-1*x));
s=Solution();
print s.reverse(123);
print s.reverse(-123);