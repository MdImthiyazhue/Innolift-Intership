# Day 4 - Task 1
# Skill Tracker using List and Tuple

# List of skills (editable)
skills = [
    "Python",
    "Data Structures",
    "HTML",
    "CSS"
]

# Tuple of fixed personal details (cannot be changed)
personal_details = (
    "Mohamed Imthiyas",
    "AI & Data Science",
    "01-07-2026"   # Internship join date
)

print("===== SKILL TRACKER =====")

print(f"First Skill : {skills[0]}")
print(f"Last Skill  : {skills[-1]}")
print(f"Total Skills: {len(skills)}")

print("\nFixed Personal Details")
print(f"Name              : {personal_details[0]}")
print(f"Department        : {personal_details[1]}")
print(f"Internship Joined : {personal_details[2]}")