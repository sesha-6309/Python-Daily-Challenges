#rr
n = int(input("how many amounts do you want to transact?"))
amount_list = []
my_dict = {"invalid":[],
           "normal":[],
           "large":[],
           "high_risk":[]
           }
total = 0

for i in range(n):
    k = int(input(f"enter the amount {i+1}:"))
    amount_list.append(k)
    if k<=0:
        my_dict["invalid"].append(k)
    elif 1<=k<=500:
        my_dict["normal"].append(k)
    elif 501<=k<=2000:
        my_dict["large"].append(k)
    else:
        my_dict["high_risk"].append(k)
valid_transactions = [l for l in amount_list if l>0] #list comprehension
total = sum(valid_transactions)


Frequent_Transactions = len(amount_list)>5
Large_spending = total>5000
Suspicious_Pattern = len(my_dict["high_risk"])>=3

#personalization
if Suspicious_Pattern or (Frequent_Transactions and Large_spending):
    risk = "High Risk"
elif Frequent_Transactions or Large_spending:
    risk = "Moderate Risk"
else:
    risk = "Low Risk"

print("valid transactions:",valid_transactions)
summary = (total, len(amount_list), risk)
print("categorized transactions:",my_dict)
print("total transaction value:", total)
print("number of transactions:",len(amount_list))
print("risk classifications:",risk)
print("summary(Total,Count,Risk):",summary)
