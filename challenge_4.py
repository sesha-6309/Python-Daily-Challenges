#rr
k = int(input("enter number of scores:"))
v_count = 0 #valid count
i_count = 0 #ignored count
reg_no = input("enter your registration number:")
D = int(reg_no[-1])
scores = [0]*k
low_risk = []
medium_risk=[]
high_risk=[]
critical_risk=[]

for i in range(k):
    n = int(input(f"enter the score of student {i+1}:"))
    scores[i] = n
    if scores[i] < 0:
        i_count +=1
    else:
        v_count +=1
        if 0 <= scores[i] <=30:
            low_risk.append(scores[i])
        elif 31 <= scores[i] <=60:
             medium_risk.append(scores[i])
        elif 61<= scores[i]<=100:
            high_risk.append(scores[i])
        else:
            critical_risk.append(scores[i])
print(f"Register Digit (D):{D}")
print("\n")
print(f"low Risk:{low_risk}")
print(f"medium risk:{medium_risk}")
print(f"high risk:{high_risk}")
print(f"critical risk:{critical_risk}")
print("\n")
print("After Personalized Filtering:")
removed_count = 0
if D%2==0:
 removed_count = len(low_risk)
 low_risk = []
else:
 removed_count = len(critical_risk)
 critical_risk = []

print(f"low risk:{low_risk}")
print(f"medium risk:{medium_risk}")
print(f"high risk:{high_risk}")
print(f"critical risk:{critical_risk}")
print("\n")
print(f"Total valid entries:{v_count}")
print(f"ignored entries:{i_count}")
print(f"Removed Due to Personalizations:{removed_count}")


