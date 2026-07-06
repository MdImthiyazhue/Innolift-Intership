import pandas as pd

# -------------------------------------------------------
# Read Datasets
# -------------------------------------------------------

students = pd.read_csv("Students.csv")
results = pd.read_csv("Results.csv")

print("=" * 70)
print("TASK 3 - MERGING")
print("=" * 70)

# -------------------------------------------------------
# Step 1
# -------------------------------------------------------

print("\nSTEP 1: Inspect Keys and Duplicates")
print("-" * 70)

print(f"Students rows : {len(students)}")
print(f"Results rows  : {len(results)}")

student_duplicates = students["Adm_No"].duplicated().sum()
result_duplicates = results["Adm_No"].duplicated().sum()

print(f"\nDuplicate Adm_No in Students : {student_duplicates}")
print(f"Duplicate Adm_No in Results  : {result_duplicates}")

# -------------------------------------------------------
# Step 2
# -------------------------------------------------------

print("\nSTEP 2: Inner Merge")
print("-" * 70)

inner_merge = pd.merge(
    students,
    results,
    on="Adm_No",
    how="inner"
)

inner_merge.to_csv("inner_merge.csv", index=False)

print(inner_merge.head())

print(f"\nRows in Inner Merge : {len(inner_merge)}")

# -------------------------------------------------------
# Step 3
# -------------------------------------------------------

print("\nSTEP 3: Left Merge")
print("-" * 70)

left_merge = pd.merge(
    students,
    results,
    on="Adm_No",
    how="left"
)

left_merge.to_csv("left_merge.csv", index=False)

students_without_results = left_merge[
    left_merge["Marks"].isna()
]

print(f"Rows in Left Merge : {len(left_merge)}")

print("\nStudents without Results:")

if students_without_results.empty:
    print("None")
else:
    print(students_without_results[["Adm_No", "Name"]])

# -------------------------------------------------------
# Step 4
# -------------------------------------------------------

print("\nSTEP 4: Outer Merge")
print("-" * 70)

outer_merge = pd.merge(
    students,
    results,
    on="Adm_No",
    how="outer"
)

outer_numeric = outer_merge.copy()

outer_numeric["Marks"] = outer_numeric["Marks"].fillna(-1)

outer_merge.to_csv("outer_merge.csv", index=False)

print(outer_numeric.head())

# -------------------------------------------------------
# Step 5
# -------------------------------------------------------

print("\nSTEP 5: Merge on Multiple Keys")
print("-" * 70)

if "Term" in results.columns:

    students_term = students.copy()

    students_term["Term"] = "Mid"

    multi_merge = pd.merge(
        students_term,
        results,
        on=["Adm_No", "Term"],
        how="left"
    )

    print(multi_merge.head())

else:
    print("Term column not available.")

# =======================================================
# QUESTIONS
# =======================================================

print("\n")
print("=" * 70)
print("ANSWERS TO QUESTIONS")
print("=" * 70)

difference = len(left_merge) - len(inner_merge)

print(f"""
Question 1
----------
How many rows differ between inner and left merges, and why?

Answer:

Difference : {difference}

Reason:
Left merge keeps every student even if they have no result.
Inner merge keeps only matching records.
""")

print("""
Question 2
----------
Show code to rename duplicate columns after merge.

Answer:

merged = pd.merge(
    df1,
    df2,
    on="Adm_No",
    suffixes=("_Student", "_Result")
)

or

merged.rename(columns={
    "Name_x":"Student_Name",
    "Name_y":"Result_Name"
}, inplace=True)
""")

print("""
Question 3
----------
When should you use Outer Merge vs Left Merge?

Answer:

Left Merge:
Use when all records from the left table must be kept.

Example:
Keep every student even if exam results are missing.

Outer Merge:
Use when records from both tables are important,
even if there is no matching key.

Example:
Combining two school databases where each contains
students missing from the other.
""")

print(f"""
Question 4
----------
If Adm_No appears multiple times in Results,
how does Inner Merge affect row counts?

Answer:

Results has {result_duplicates} duplicate Adm_No values.

Each matching record creates a new row in the merged
DataFrame.

Therefore, one student can appear multiple times
(one row for each subject).
""")