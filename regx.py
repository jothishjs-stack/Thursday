import re
txt = "The rain 45 in Spain stays mainly in the plain"
x = re.search("ai",txt)
if x:  print("Yes, there is at least one match!")   
else:  print("No match")
x=re.findall("\d",txt)
print(x)