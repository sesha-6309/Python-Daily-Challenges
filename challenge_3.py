N = int(input("enter number of students written the exam:"))
marks = [0]*N
count = 0
f_count = 0
name = input("enter name:")
name_len = len(name)
for i in range(N):
    marks[i] = int(input(f"enter student {i+1} marks:"))
    if marks[i] < 0 or marks[i] > 100:
        print(f"{marks[i]} -> Invalid")
    else:

        if name_len%2==0 and 35 <=marks[i]<= 39:
             marks[i] = 40 #personalized grace marks added to the students who got nearly the pass marks
        if 90<=marks[i]<=100:
            print(f"{marks[i]}->Excellent")
            count+=1
        elif 75<=marks[i]<=89:
            print(f"{marks[i]}->Very Good")
            count += 1
        elif 60<=marks[i]<=74:
            print(f"{marks[i]}->Good")
            count += 1
        elif 40<=marks[i]<=59:
             print(f"{marks[i]}->Average")
             count += 1
        elif 0<=marks[i]<=34:
             print(f"{marks[i]}->Fail")
             count += 1
             f_count+= 1
print(f"Total Valid Students: {count}")
print(f"Total Failed Students: {f_count}")
