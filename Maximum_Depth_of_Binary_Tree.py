# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
    # @param root, a tree node
    # @return an integer
	def maxDepth(self, root):
		if(root == None):
			return 0;
		return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right));
a=TreeNode(1);
b=TreeNode(2);
c=TreeNode(3);
a.left=b;
b.left=c;
s=Solution();
print s.maxDepth(a);
