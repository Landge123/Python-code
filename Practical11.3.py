def test(s):
 upper=0
 lower=0
 for i in s:
  if(i.islower()):
   lower=lower+1
 else:
    upper=upper+1
 print("Lower case=",lower)
 print("Upper case=",upper)
s=input("Enter string: ")
test(s)
