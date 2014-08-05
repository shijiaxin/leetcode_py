import COMMON
class Solution:
	# @param root, a tree node
	# @param sum, an integer
	# @return a boolean
	def hasPathSum(self, root, sum):
		if root==None:
			return False;
		if root.left==None and root.right==None and root.val==sum:
			return True;
		if (self.hasPathSum(root.left,sum-root.val)):
			return True;
		if (self.hasPathSum(root.right,sum-root.val)):
			return True;
		return False;
s=Solution();
print s.hasPathSum(COMMON.build_tree("{5,4,8,11,#,13,4,7,2,#,#,#,1}"),22);
print s.hasPathSum(COMMON.build_tree("{5,4,8,11,#,13,4,7,2,#,#,#,1}"),21);
