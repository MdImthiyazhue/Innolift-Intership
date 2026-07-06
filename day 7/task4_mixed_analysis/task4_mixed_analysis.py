import pandas as pd

# -------------------------------------------------------
# Read Datasets
# -------------------------------------------------------

students = pd.read_csv("Students.csv")
results = pd.read_csv("Results.csv")
attendance = pd.read_csv("Attendance.csv")

print("=" * 70)
print("TASK 4 - MIXED ANALYSIS")
print("=" * 70)

# -------------------------------------------------------
# Step 1
# -------------------------------------------------------

print("\nSTEP 1: Clean Missing Attendance")
print("-" * 70)

attendance["Present"] = attendance["Present"].fillna(False)

print("Missing values after cleaning:")
print(attendance.isnull().sum())

# -------------------------------------------------------
# Step 2
# -------------------------------------------------------

print("\nSTEP 2: Filter Final Term Results")
print("-" * 70)

filtered_results = results[results["Term"] == "Final"]

print(f"Rows in Final Term : {len(filtered_results)}")

# -------------------------------------------------------
# Step 3
# -------------------------------------------------------

print("\nSTEP 3: Student Scores")
print("-" * 70)

student_scores = (
    filtered_results
    .groupby("Adm_No")
    .agg(
        total_marks=("Marks", "sum"),
        avg_marks=("Marks", "mean")
    )
    .reset_index()
)

print(student_scores.head())

# -------------------------------------------------------
# Step 4
# -------------------------------------------------------

print("\nSTEP 4: Attendance Rate")
print("-" * 70)

attendance_summary = (
    attendance
    .groupby("Adm_No")
    .agg(
        attendance_rate=("Present", "mean")
    )
    .reset_index()
)

attendance_summary["attendance_rate"] *= 100

attendance_summary.to_csv(
    "student_attendance.csv",
    index=False
)

print(attendance_summary.head())

# -------------------------------------------------------
# Step 5
# -------------------------------------------------------

print("\nSTEP 5: Final Report")
print("-" * 70)

final_report = (
    students
    .merge(student_scores, on="Adm_No", how="left")
    .merge(attendance_summary, on="Adm_No", how="left")
)

final_report.to_csv(
    "final_report.csv",
    index=False
)

print(final_report.head())

# -------------------------------------------------------
# Step 6
# -------------------------------------------------------

print("\nSTEP 6: At-Risk Students")
print("-" * 70)

at_risk = final_report[
    (final_report["attendance_rate"] < 75) &
    (final_report["avg_marks"] < 40)
]

at_risk.to_csv(
    "at_risk.csv",
    index=False
)

print(at_risk)

# =======================================================
# QUESTIONS
# =======================================================

print("\n")
print("=" * 70)
print("ANSWERS TO QUESTIONS")
print("=" * 70)

top5 = (
    final_report
    .sort_values(
        by="avg_marks",
        ascending=False
    )
    .head(5)
)

print("""
Question 1
----------
Which 5 students have the highest average Marks
and what are their attendance rates?

Answer:
""")

print(
    top5[
        [
            "Adm_No",
            "Name",
            "avg_marks",
            "attendance_rate"
        ]
    ]
)

print(f"""
Question 2
----------
How many students are at risk?

Answer:

{len(at_risk)}
""")

print("""
Question 3
----------
Explain how incorrect handling of missing attendance
would bias attendance_rate.

Answer:

If missing attendance is ignored or treated incorrectly,
attendance percentages may become artificially high or
low. Filling missing values consistently prevents
misleading attendance calculations.
""")

print("""
Question 4
----------
Provide code to export final_report.csv with
Percentage rounded to 2 decimals.

Answer:

final_report["avg_marks"] = \
final_report["avg_marks"].round(2)

final_report.to_csv(
    "final_report.csv",
    index=False
)
""")

print("""
Question 5
----------
If Adm_No has different data types
(int vs string), what problems occur?

Answer:

Merge operations will fail because the keys
will not match.

Fix:

students["Adm_No"] = students["Adm_No"].astype(int)

results["Adm_No"] = results["Adm_No"].astype(int)

or convert both to string before merging.
""")