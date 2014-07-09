class Solution:
	def smallToRoman(self,str,num):
		if (num <= 3):
			return str[0]*num;
		if (num == 4):
			return str[0]+str[1];
		if (num <= 8):
			return str[1]+str[0]*(num-5);
		return str[0]+str[2];
	# @return an integer
	def romanToInt(self, s):
		arr=["IVX","XLC","CDM","M??"];
		result=0;
		# first handle number more than 1000
		for i in range(3,0,-1):
			str=self.smallToRoman(arr[3],i);
			if(s[0:len(str)]==str):
				s=s[len(str):];
				result+=i*1000;
				break;
		for k in range(2,-1,-1):
			for i in range(9,0,-1):
				str=self.smallToRoman(arr[k],i);
				if(s[0:len(str)]==str):
					s=s[len(str):];
					result+=i*(10**k);
					break;
		return result;
s=Solution();
print s.romanToInt("XCVIII");
print s.romanToInt("MDCCCLXXXVIII");
print s.romanToInt("MMMCMXCIX");

