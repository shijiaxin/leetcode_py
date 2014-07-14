# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
	def getHeight(self,root):
		if(root==None):
			return 0;
		l=self.getHeight(root.left);
		r=self.getHeight(root.right);
		if(l==-1 or r == -1):
			return -1;
		if((l>r+1) or (r>l+1)):
			return -1;
		return max(l,r)+1;
	# @param root, a tree node
	# @return a boolean
	def isBalanced(self, root):
		if(self.getHeight(root)==-1):
			return False;
		return True;
a1=TreeNode(1);
a2=TreeNode(2);
a3=TreeNode(3);
a4=TreeNode(4);
a5=TreeNode(5);
a6=TreeNode(6);
a1.left=a2;
a1.right=a3;
a3.left=a4;
a3.right=a5;
a5.left=a6;
s=Solution();
print s.isBalanced(a3);
print s.isBalanced(a1);
