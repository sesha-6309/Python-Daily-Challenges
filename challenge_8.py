import random
import math
import numpy as np
import pandas as pd

def generate_data(n):
    students = []
    
    for i in range(1, n+1):
        student_id = f"S{i}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)
        
        performance_index = (marks * 0.6 + assignment * 0.4) * math.log(attendance + 1)
        
        students.append((student_id, marks, attendance, assignment, performance_index))
    
    return students

def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }
    
    for student in data:
        sid, marks, attendance, assignment, pi = student
        
        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)
        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)
        elif 71 <= marks <= 90:
            categories["Good"].append(sid)
        else:
            categories["Average"].append(sid)
    
    return categories


def analyze_data(df):
    marks_array = np.array(df['Marks'])
    
    # Mean (NumPy)
    mean_marks = np.mean(marks_array)
    
    # Median (NumPy)
    median_marks = np.median(marks_array)
    
    # Standard Deviation (Manual)
    mean_manual = sum(marks_array) / len(marks_array)
    variance = sum((x - mean_manual) ** 2 for x in marks_array) / len(marks_array)
    std_dev = math.sqrt(variance)
    
    # Correlation
    correlation = df['Marks'].corr(df['Attendance'])
    
    # Normalization
    min_val = np.min(marks_array)
    max_val = np.max(marks_array)
    df['Normalized Marks'] = [(x - min_val) / (max_val - min_val) for x in marks_array]
    
    # Pattern Detection
    consistency = "Consistent" if std_dev < 15 else "Inconsistent"
    
    low_attendance = len([x for x in df['Attendance'] if x < 50])
    attendance_risk = low_attendance > 3
    
    top_performers = len([x for x in df['Marks'] if x > 90])
    high_achievement = top_performers >= 2
    
    # Final Insight
    if consistency == "Consistent" and not attendance_risk:
        system_status = "Stable Academic System"
    elif high_achievement:
        system_status = "Moderate Performance"
    else:
        system_status = "Critical Attention Required"
    
    summary_tuple = (mean_marks, std_dev, max_val)
    
    return {
        "mean": mean_marks,
        "median": median_marks,
        "std_dev": std_dev,
        "correlation": correlation,
        "consistency": consistency,
        "attendance_risk": attendance_risk,
        "high_achievement": high_achievement,
        "system_status": system_status,
        "tuple": summary_tuple
    }


# Rule: last digit of roll number (example: 3 → 10+3 = 13 students)
n = 12  # Change this based on your roll number rule

data = generate_data(n)

# Convert to DataFrame
df = pd.DataFrame(data, columns=[
    "Student_ID", "Marks", "Attendance", "Assignment", "Performance_Index"
])

# Classification
categories = classify_students(data)

# Analysis
results = analyze_data(df)

print("\n===== STUDENT DATA =====")
print(df)

print("\n===== CLASSIFICATION =====")
for key, value in categories.items():
    print(f"{key}: {value}")

print("\n===== STATISTICAL SUMMARY =====")
print(f"Mean: {results['mean']}")
print(f"Median: {results['median']}")
print(f"Standard Deviation: {results['std_dev']}")
print(f"Correlation (Marks vs Attendance): {results['correlation']}")

print("\n===== TUPLE OUTPUT =====")
print(results["tuple"])

print("\n===== SYSTEM INSIGHT =====")
print(results["system_status"])