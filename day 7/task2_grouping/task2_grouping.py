import pandas as pd
import numpy as np

# -------------------------------------------------------
# Read Dataset
# -------------------------------------------------------

df = pd.read_csv("Exam_scores.csv")

print("=" * 70)
print("TASK 2 - GROUPING & AGGREGATION")
print("=" * 70)

# -------------------------------------------------------
# Step 1
# -------------------------------------------------------

print("\nSTEP 1: DataFrame Information")
print("-" * 70)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

# -------------------------------------------------------
# Step 2
# -------------------------------------------------------

print("\nSTEP 2: Fill Missing Marks")
print("-" * 70)

missing_before = df["Marks"].isna().sum()

rows_changed = df[df["Marks"].isna()].copy()

# Fill missing marks using subject-wise mean
df["Marks"] = df.groupby("Subject")["Marks"].transform(
    lambda x: x.fillna(x.mean())
)

# If any subject still has NaN, replace with 0
df["Marks"] = df["Marks"].fillna(0)

missing_after = df["Marks"].isna().sum()

print(f"Missing values before filling : {missing_before}")
print(f"Missing values after filling  : {missing_after}")
print(f"Rows updated                  : {len(rows_changed)}")

# -------------------------------------------------------
# Step 3
# -------------------------------------------------------

print("\nSTEP 3: Subject-wise Summary")
print("-" * 70)

subject_summary = (
    df.groupby("Subject")["Marks"]
      .agg(["count", "mean", "min", "max"])
      .reset_index()
)

subject_summary.to_csv("subject_summary.csv", index=False)

print(subject_summary)

# -------------------------------------------------------
# Step 4
# -------------------------------------------------------

print("\nSTEP 4: Class-wise Average Marks")
print("-" * 70)

class_average = (
    df.groupby("Class")["Marks"]
      .mean()
      .reset_index(name="Average Marks")
)

print(class_average)

# -------------------------------------------------------
# Step 5
# -------------------------------------------------------

print("\nSTEP 5: Top 3 Students by Total Marks")
print("-" * 70)

student_totals = (
    df.groupby(["Adm_No", "Name"])["Marks"]
      .sum()
      .reset_index(name="Total Marks")
)

top3 = student_totals.sort_values(
    by="Total Marks",
    ascending=False
).head(3)

print(top3)

# =======================================================
# QUESTIONS
# =======================================================

print("\n")
print("=" * 70)
print("ANSWERS TO QUESTIONS")
print("=" * 70)

print(f"""
Question 1
----------
How many missing Marks were filled and what value(s) were used?

Answer:

Missing values filled : {missing_before}

Method used:
Subject-wise mean.
If a subject had no valid marks, 0 was used.
""")

highest_subject = subject_summary.loc[
    subject_summary["mean"].idxmax(),
    "Subject"
]

highest_mean = subject_summary["mean"].max()

print(f"""
Question 2
----------
Which subject has the highest mean Marks?

Answer:

Subject : {highest_subject}

Mean Marks : {highest_mean:.2f}
""")

print("""
Question 3
----------
Show the code to convert a multi-aggregation result into a flat DataFrame.

Answer:

summary = (
    df.groupby("Subject")["Marks"]
      .agg(["count","mean","min","max"])
      .reset_index()
)

reset_index() converts the grouped result back into a normal DataFrame.
""")

print("""
Question 4
----------
Why is reset_index() often necessary after groupby()?

Answer:

groupby() stores the grouped column as the index.

reset_index() converts that index back into a normal column,
making the DataFrame easier to print, merge, filter,
and export to CSV.
""")