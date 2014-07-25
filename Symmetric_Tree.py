# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	def helper(self,l,r):
		if(l==None and r == None):
			return True;
		if(l==None or  r == None):
			return False;
		if(l.val!=r.val):
			return False;
		if(self.helper(l.left,r.right) and self.helper(l.right,r.left)):
			return True;
		return False;
	# @param root, a tree node
	# @return a boolean
	def isSymmetric(self, root):
		return self.helper(root,root);
