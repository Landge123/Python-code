s=(input("enter the String:"))
lower=0
upper=0
for i in s:
    if(i.islower()):
            lower+=1
    else:
            upper+=1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)