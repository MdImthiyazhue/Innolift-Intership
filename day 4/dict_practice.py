# Day 4 - Task 2
# Dictionary Practice

# Create a dictionary for one student
student = {
    "name": "Mohamed Imthiyas",
    "subject": "Python",
    "score": 82,
    "status": "Distinction"
}

print("===== STUDENT DETAILS =====")
print(f"Name    : {student['name']}")
print(f"Subject : {student['subject']}")
print(f"Score   : {student['score']}")
print(f"Status  : {student['status']}")

# Update the score
student["score"] = 91

print("\n===== UPDATED STUDENT RECORD =====")
print(student)