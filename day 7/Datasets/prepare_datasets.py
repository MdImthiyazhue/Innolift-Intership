import pandas as pd
import numpy as np

# -----------------------------
# Read Original Dataset
# -----------------------------
df = pd.read_csv("Student_Performance.csv")

# -----------------------------
# Create Common Columns
# -----------------------------
df["Adm_No"] = df["student_id"]

df["Name"] = [
    f"Student_{i}" for i in df["Adm_No"]
]

classes = ["I", "II", "III"]
df["Class"] = [classes[i % 3] for i in range(len(df))]

df["Gender"] = df["gender"].str.capitalize()

# ======================================================
# STUDENTS.CSV
# ======================================================

students = df[
    ["Adm_No", "Name", "Gender", "Class"]
]

students.to_csv("Students.csv", index=False)

# ======================================================
# STUDENT_RESULTS.CSV
# ======================================================

subject_frames = []

subject_map = {
    "Maths": "math_score",
    "Science": "science_score",
    "English": "english_score"
}

for subject, column in subject_map.items():

    temp = pd.DataFrame({
        "Adm_No": df["Adm_No"],
        "Name": df["Name"],
        "Class": df["Class"],
        "Gender": df["Gender"],
        "Subject": subject,
        "Marks": df[column],
        "Percentage": df["overall_score"]
    })

    subject_frames.append(temp)

student_results = pd.concat(subject_frames, ignore_index=True)

student_results.to_csv("Student_results.csv", index=False)

# ======================================================
# EXAM_SCORES.CSV
# ======================================================

exam_scores = student_results.copy()

exam_scores["Term"] = np.where(
    exam_scores.index % 2 == 0,
    "Mid",
    "Final"
)

# Add some missing values intentionally
np.random.seed(42)

missing_rows = np.random.choice(
    exam_scores.index,
    200,
    replace=False
)

exam_scores.loc[missing_rows, "Marks"] = np.nan

exam_scores.to_csv("Exam_scores.csv", index=False)

# ======================================================
# RESULTS.CSV
# ======================================================

results = exam_scores[
    [
        "Adm_No",
        "Subject",
        "Marks",
        "Percentage",
        "Term"
    ]
]

results.to_csv("Results.csv", index=False)

# ======================================================
# ATTENDANCE.CSV
# ======================================================

attendance = []

for _, row in df.iterrows():

    present = row["attendance_percentage"] >= 75

    attendance.append({
        "Adm_No": row["Adm_No"],
        "Date": "2026-07-01",
        "Present": present
    })

attendance_df = pd.DataFrame(attendance)

attendance_df.to_csv("Attendance.csv", index=False)

print("\nDatasets Created Successfully!\n")

print("Generated Files:")
print("-------------------------------")
print("Students.csv")
print("Student_results.csv")
print("Exam_scores.csv")
print("Results.csv")
print("Attendance.csv")