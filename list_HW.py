numbers = [1, 2, 3, 4, 5, 5]
#1 pop ()
numbers.pop() 
print("The numbers are: ", numbers)

#2 squares 
sqnumbers=[x**2 for x in range(10)]
print("Square values are: ",sqnumbers)

#3 append an ACL line
acl = [
    "permit ip any 192.168.10.0 0.0.0.255",
    "permit ip any 192.168.20.0 0.0.0.255",
    "permit tcp any any eq 80",
    "permit tcp any any eq 443",
    "permit udp any any eq 53",
    "permit ip any any"
]
ssh_acl = "permit tcp any any eq 22"
acl.append(ssh_acl)
print("updated ACL is: ",acl)

#4 for loop in list
for x in acl:
    print(x)

#5 finding an ACL using for and if
findacl=[]
for y in acl:
 if "tcp" in y:
    findacl.append(y)
    print("tcp connections are : ",findacl)

# rewriting condition with UDP
udpdacl=[z for z in acl if "udp" in z]
print("udp contains in : ", udpdacl)