# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if((p==None) & (q==None)):
            return True;
        if((p==None) | (q==None)):
            return False;
        if(p.val != q.val):
            return False;
        if(self.isSameTree(p.left,q.left) & self.isSameTree(p.right,q.right)):
            return True;
        return False;

a=TreeNode(1);
b=TreeNode(2);
c=TreeNode(3);
a.left=b;
b.left=c;
s=Solution();
print s.isSameTree(a,a);
print s.isSameTree(a,b);