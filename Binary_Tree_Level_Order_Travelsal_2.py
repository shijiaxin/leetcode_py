import COMMON;
class Solution:
	# @param root, a tree node
	# @return a list of lists of integers
	def levelOrderBottom(self, root):
		if(root==None):
			return [];
		data=[[root]];
		while(True):
			next=[];
			for node in data[len(data)-1]:
				if(node.left!=None):
					next+=[node.left];
				if(node.right!=None):
					next+=[node.right];
			if(next!=[]):
				data+=[next];
			else:
				break;
		for arr in data:
			size=0;
			while(size<len(arr)):
				arr[size]=arr[size].val;
				size+=1;
		data.reverse();
		return data;
s=Solution();
print s.levelOrderBottom(COMMON.build_tree("{3,9,20,#,#,15,7}"))
