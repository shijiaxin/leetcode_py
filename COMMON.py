class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
def print_tree(node):
	if(node==None):
		print [];
	data=[node];
	pos=0;
	while(pos<len(data)):
		if(data[pos]!=None):
			data+=[data[pos].left];
			data+=[data[pos].right];
		pos+=1;
	for i in range(len(data)):
		if(data[i]!=None):
			data[i]=data[i].val;
	print data; 
def build_tree(str):
	data=str[1:-1].split(",");
	if(data==[""]):
		return None;
	n=len(data);
	i=0;
	while(i<n):
		if(data[i]=="#"):
			data[i]=None;
		else:
			data[i]=TreeNode(int(data[i]));
		i+=1;
	i=1;parent=0;
	while(True):
		if(i<n):
			data[parent].left=data[i];	
		i+=1;
		if(i<n):
			data[parent].right=data[i];	
		i+=1;
		parent+=1;
		while(parent<n and data[parent]==None):
			parent+=1;
		if(i>=n or parent>= n):
			break;
	return data[0];






