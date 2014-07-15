# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
class Solution:
	def sortedArrayToBSTrecursive(self,num,begin,end):
		if(begin>=end):
			return None;
		middle=(end-begin)/2+begin;
		node=TreeNode(num[middle]);
		l=self.sortedArrayToBSTrecursive(num,begin,middle);
		r=self.sortedArrayToBSTrecursive(num,middle+1,end);
		node.left=l;
		node.right=r;
		return node;
	# @param num, a list of integers
	# @return a tree node
	def sortedArrayToBST(self, num):
		return self.sortedArrayToBSTrecursive(num,0,len(num));

