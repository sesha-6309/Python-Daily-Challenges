s_id = input("ID:")
e_id = input("Email:")
pw = input("Password:")
r_code = input("Referral:")
l = len(e_id)
if len(s_id)==7 and s_id[0:4] =="CSE-" and s_id[4:].isdigit():
    if e_id.count("@")==1 and e_id.count(".")>0 and e_id[0]!="@" and e_id[l-1]!="@" and e_id[-4:]==".edu":
      if len(pw)>=8 and pw[0].isupper() and (pw.count('0')>0 or pw.count('1')>0 or pw.count('2')>0 or pw.count('3')>0 or pw.count('4')>0 or pw.count('5')>0 or pw.count('6')>0 or pw.count('7')>0 or pw.count('8')>0 or pw.count('9')>0):
          if len(r_code)==6 and r_code[0:3]=="REF" and r_code[3:5].isdigit() and r_code[5]=="@":
              print("APPROVED")
          else:
              print("REJECTED")
      else:
          print("REJECTED")
    else:
        print("REJECTED")
else:
    print("REJECTED")





