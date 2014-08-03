class Solution:
	# @return a boolean
	def isValid(self, s):
		array=[];
		for c in s:
			if(c=="(" or c=="{" or c=="["):
				array.append(c);
			elif (array==[]):
				return False;
			else: 
				first=array.pop();
				if(first=="(" and c==")"):
					continue;
				if(first=="{" and c=="}"):
					continue;
				if(first=="[" and c=="]"):
					continue;
				return False;
		if(array==[]):
			return True;
		return False;
s=Solution();
print s.isValid("()[]{}");
print s.isValid("([)]");
				
				
