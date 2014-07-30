import COMMON
class Solution:
	def helper(self,root):
		if(root==None):
			return (0,0);
		if(root.left==None and root.right==None):
			return (1,root.val);
		l=self.helper(root.left);
		r=self.helper(root.right);
		return ((l[0]+r[0])*10,root.val*10*(l[0]+r[0])+l[1]+r[1]);
	# @param root, a tree node
	# @return an integer
	def sumNumbers(self, root):
		return self.helper(root)[1];

s=Solution();
print s.sumNumbers(COMMON.build_tree("{1,2,3}"));
print s.sumNumbers(COMMON.build_tree("{1,2,3,4}"));	
