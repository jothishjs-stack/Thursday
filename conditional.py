a=10
b=20
# input("Enter a value for a: ")
# input("Enter a value for b: ")
if a > b:
    print("a is greater than b")
    #nested if statement elif
elif a < b:
    print("a is less than b")   
else:
    print("a is equal to b")    



if(a%2==0):
    print("a is even")
else:
    print("a is odd")

is_logged_in=True
if is_logged_in:
    print("User is logged in")
else:
    print("User is not logged in")  
# change all variable in single line > check online

num=10
match num:
    case 1:
        print("Number is one")
    case 2:
        print("Number is two")
    case 3:
        print("Number is three")
    case _:
        print("Number is not listed there")