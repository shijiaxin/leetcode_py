class Solution:
	def charToInt(self,s):
		arr="IVXLCDM";
		intarr=[1,5,10,50,100,500,1000];
		pos=arr.find(s);
		if(pos>=0 & pos<len(intarr)):
			return intarr[pos];
		return 0;
	# @return an integer
	def romanToInt(self, s):
		arr=["IVX","XLC","CDM","M??"];
		result=0;
		last=0;
		for c in s:
			r=self.charToInt(c);
			if(r==(last*10) or r==(last*5)):
				result-=2*last;
			result+=r;
			last=r;
		return result;
s=Solution();
print s.romanToInt("XCVIII");
print s.romanToInt("MDCCCLXXXVIII");
print s.romanToInt("MMMCMXCIX");

