import COMMON
class Solution:
	def helper(self,root):
		if root==None:
			return (True,None,None);
		l=self.helper(root.left);
		r=self.helper(root.right);
		if not (l[0] and r[0]):
			return (False,None,None);
		res_bool,res_l,res_r=True,root,root;
		if l[2]!=None :
			if l[2].val >= root.val:
				res_bool=False;
			res_l=l[1];
		if r[2]!=None :
			if r[1].val <= root.val:
				res_bool=False;
			res_r=r[2];
		return (res_bool,res_l,res_r);
	# @param root, a tree node
	# @return a boolean
	def isValidBST(self, root):
		return self.helper(root)[0];
s=Solution();
print s.isValidBST(COMMON.build_tree("{1,#,2,#,3}"));
print s.isValidBST(COMMON.build_tree("{1,2,3}"));
