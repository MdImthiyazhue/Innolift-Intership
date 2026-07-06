import pandas as pd

# Read Dataset
df = pd.read_csv("Student_results.csv")

print("=" * 70)
print("TASK 1 - FILTERING")
print("=" * 70)

# -------------------------------------------------------
# Step 1
# -------------------------------------------------------
print("\nSTEP 1: Read CSV")
print("-" * 70)

print(f"Shape of DataFrame : {df.shape}")

print("\nFirst 5 Rows:")
print(df.head())

# -------------------------------------------------------
# Step 2
# -------------------------------------------------------
print("\nSTEP 2: Percentage Series")
print("-" * 70)

percentage_series = df["Percentage"]

print(percentage_series.head())

# -------------------------------------------------------
# Step 3
# -------------------------------------------------------
print("\nSTEP 3: Percentage >= 75")
print("-" * 70)

high_percentage = df[df["Percentage"] >= 75]

high_percentage.to_csv("filtered_high.csv", index=False)

print(f"Students Found : {len(high_percentage)}")
print("Saved as filtered_high.csv")

# -------------------------------------------------------
# Step 4
# -------------------------------------------------------
print("\nSTEP 4: Maths Marks < 40")
print("-" * 70)

maths_failed = df[
    (df["Subject"] == "Maths") &
    (df["Marks"] < 40)
]

print(f"Students Found : {len(maths_failed)}")

print(maths_failed[["Adm_No", "Name", "Marks"]])

# -------------------------------------------------------
# Step 5
# -------------------------------------------------------
print("\nSTEP 5: Query")
print("-" * 70)

female_class2 = df.query(
    "Gender == 'Female' and Class == 'II' and Percentage > 60"
)

print(female_class2)

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
How many students have Percentage >= 75?

Answer:
{len(high_percentage)}
""")

print(f"""
Question 2
----------
What is the average Percentage of the filtered group?

Answer:
{high_percentage['Percentage'].mean():.2f}
""")

print("""
Question 3
----------
Which Maths students scored below 40?

Answer:
""")

print(maths_failed[["Adm_No", "Name"]])

print("""
Question 4
----------
Explain when you would use .loc vs .iloc.

Answer:

.loc
• Uses row/column labels.
• Can filter using conditions.
Example:
df.loc[df["Marks"] > 50]

.iloc
• Uses integer positions.
• Used when selecting rows by index.
Example:
df.iloc[0:5]
""")