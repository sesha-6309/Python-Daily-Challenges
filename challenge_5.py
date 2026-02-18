#rr
m = int(input("enter how many requests:"))
requests = [0]*m
low_demand = []
moderate_demand = []
high_demand = []
invalid_requests = []

v_count = 0#valid count
i_count = 0#invalid requests
name = input("enter your name:")
L = 0
for k in name:
    if k!=" ":
        L+=1

PLI = L%3
for i in range(m):
    n = int(input(f"enter the request from zone {i+1}:"))
    requests[i] = n
    if requests[i]<0:
        invalid_requests.append(n)#n can also be replaced by requests[i]
        i_count+=1
    else:
        v_count+=1
        if 1<=requests[i]<=20:
            low_demand.append(n)
        elif 21<=requests[i]<=50:
            moderate_demand.append(n)
        elif requests[i]>50  :
            high_demand.append(n)
print("\n")
print("-----BEFORE FILTRATION-----")
print(f"low_demand = {low_demand}")
print(f"moderate_demand = {moderate_demand}")
print(f"high_demand = {high_demand}")
print(f"invalid_requests = {invalid_requests}")
print("\n")
print(f"Total valid requests:{v_count}")
l = 0
if PLI == 0:
    l = len(low_demand)
    low_demand = []
    print("PLI = 0 -> RULE A")
elif PLI == 1:
    l = len(high_demand)
    high_demand = []
    print("PLI = 1 -> RULE B")
else:
    l1 = len(low_demand)
    l2 = len(high_demand)
    l = l1 + l2
    low_demand = []
    high_demand = []
    print("PLI = 2 -> RULE C")

print(f"removed requests due to PLI:{l}")
print(f"L : {L}")
print(f"PLI : {PLI}")
print("-----AFTER FILTRATION-----")
print(f"low_demand = {low_demand}")
print(f"moderate_demand = {moderate_demand}")
print(f"high_demand = {high_demand}")
print(f"invalid_requests = {invalid_requests}")



