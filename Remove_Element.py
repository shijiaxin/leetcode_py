class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
    	l=len(A);
    	pos=0;
    	while(pos<l):
    		if(A[pos]==elem):
    			A[pos],A[l-1]=A[l-1],A[pos];
    			l=l-1;
    		else:
    			pos=pos+1;
    	return l;