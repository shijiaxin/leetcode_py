class Solution:
    def smallToRoman(self,str,num):
        if (num <= 3):
            return str[0]*num;
        if (num == 4):
            return str[0]+str[1];
        if (num <= 8):
            return str[1]+str[0]*(num-5);
        return str[0]+str[2];
    # @return a string
    def intToRoman(self, num):
        arr=["IVX","XLC","CDM","M??"];
        pos=0;
        res="";
        while(num>0):
            cur=num%10;
            res=self.smallToRoman(arr[pos],cur)+res;
            num=num/10;
            pos+=1;
        return res;
s=Solution();
print s.intToRoman(98);
print s.intToRoman(1888);
print s.intToRoman(3999);
