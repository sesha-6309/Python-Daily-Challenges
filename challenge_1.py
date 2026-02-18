Fn = input("enter the full name:")
e_id = input("enter the email id:")
mob_num = input("enter your mobile number:")
age = int(input("enter your age:"))
l = len(Fn)
if Fn.count(" ")>0 and Fn[0]!=" " and Fn[l-1]!=" ":
    if e_id.count("@")>0 and e_id.count(".")>0 and e_id[0]!="@":
        if len(mob_num)==10 and mob_num[0]!='0' and mob_num.isdigit():
            if age>=18 and age<=60:
                print("User profile is VALID")
            else:
                print("User profile is INVALID")
        else:
            print("User profile is INVALID")
    else:
        print("User profile is INVALID")
else:
    print(" User profile is INVALID")


