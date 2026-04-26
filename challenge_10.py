import random
import math
import copy
import numpy as np
import pandas as pd

def create_data(n):
    data = []
    for i in range(n):
        d = {
            "id": i + 1,
            "marks": random.randint(40, 100),
            "attendance": random.randint(60, 100),
            "scores": [random.randint(10, 30), random.randint(10, 30)]
        }
        data.append(d)
    return data


def change_data(data, mod_val):
    for i in range(len(data)):
        if i % mod_val == 0:
            m = data[i]["marks"]
            data[i]["marks"] = m + math.sqrt(m)

            # change inner list
            data[i]["scores"][0] += 5

            # reduce attendance
            data[i]["attendance"] -= 5



def get_stats(original, modified):
    orig_marks = [x["marks"] for x in original]
    mod_marks = [x["marks"] for x in modified]

    mean_orig = np.mean(orig_marks)
    mean_mod = np.mean(mod_marks)
    std_dev = np.std(mod_marks)

    # manual mean (no numpy)
    manual_mean = sum(orig_marks) / len(orig_marks)

    drift = abs(mean_orig - mean_mod)

    return mean_orig, mean_mod, std_dev, drift, manual_mean


def final_result(drift, threshold, original, shallow):
    if original != shallow:
        return "Copy Failure Detected"
    elif drift < threshold:
        return "Stable Data"
    elif drift < threshold * 2:
        return "Minor Drift"
    else:
        return "Critical Drift"



n = random.randint(10, 15)
students = create_data(n)

print("\nOriginal Data:")
print(pd.DataFrame(students))


shallow = copy.copy(students)
deep = copy.deepcopy(students)

roll_no = 23
mod_val = roll_no % 3
if mod_val == 0:
    mod_val = 1


change_data(shallow, mod_val)
change_data(deep, mod_val)

mean_o, mean_d, std_d, drift, manual_mean = get_stats(students, deep)

# normalize marks
marks = np.array([x["marks"] for x in deep])
norm = (marks - min(marks)) / (max(marks) - min(marks))

threshold = 2
result = final_result(drift, threshold, students, shallow)

print("\nShallow Copy:")
print(pd.DataFrame(shallow))

print("\nDeep Copy:")
print(pd.DataFrame(deep))

print("\nDrift:", drift)
print("Tuple:", (mean_d, drift, std_d))
print("Manual Mean:", manual_mean)

print("\nNormalized Marks:", norm)

print("\nFinal Result:", result)