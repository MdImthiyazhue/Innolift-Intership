# ==========================================
# GradeVault - Student Score Manager
# Day 4 Main Project
# ==========================================

from grade_utils import PASS_CUTOFFS

# ------------------------------------------
# Student Database
# (Status is generated automatically)
# ------------------------------------------
students = [
    {"name": "Alice", "subject": "Python", "score": 82},
    {"name": "Bob", "subject": "Python", "score": 58},
    {"name": "Charlie", "subject": "DSA", "score": 30},
    {"name": "David", "subject": "DSA", "score": 91},
    {"name": "Eva", "subject": "Python", "score": 67}
]


# ------------------------------------------
# Determine Student Status
# ------------------------------------------
def calculate_status(score):
    if score >= PASS_CUTOFFS[2]:
        return "Distinction"
    elif score >= PASS_CUTOFFS[1]:
        return "Pass"
    else:
        return "Fail"


# ------------------------------------------
# Return Unique Subjects (Set)
# ------------------------------------------
def unique_subjects():
    return {student["subject"] for student in students}


# ------------------------------------------
# Add New Student
# ------------------------------------------
def add_student(name, subject, score):

    status = calculate_status(score)

    student = {
        "name": name,
        "subject": subject,
        "score": score,
        "status": status
    }

    students.append(student)

    # Save into log file
    with open("grades_log.txt", "a") as file:
        file.write(
            f"{name}, {subject}, {score}, {status}\n"
        )

    print(f"\n{name} added successfully!")


# ------------------------------------------
# Display All Students
# ------------------------------------------
def list_students():

    print("\n==================== GRADEVAULT ====================")
    print(f"{'Name':<12}{'Subject':<12}{'Score':<8}{'Status'}")
    print("----------------------------------------------------")

    for student in students:

        # Automatically calculate status
        status = calculate_status(student["score"])

        # Store the status back into dictionary
        student["status"] = status

        print(
            f"{student['name']:<12}"
            f"{student['subject']:<12}"
            f"{student['score']:<8}"
            f"{student['status']}"
        )

    print("====================================================")


# ------------------------------------------
# Calculate Average for One Subject
# ------------------------------------------
def class_average(subject):

    # Store scores of selected subject
    scores = []

    # Filter matching students
    for student in students:
        if student["subject"].lower() == subject.lower():
            scores.append(student["score"])

    # Prevent division by zero
    if len(scores) == 0:
        return 0

    # Return average score
    return sum(scores) / len(scores)


# ------------------------------------------
# Find Highest Scorer
# ------------------------------------------
def top_scorer():

    # Assume first student is highest
    highest = students[0]

    # Compare every student's score
    for student in students:
        if student["score"] > highest["score"]:
            highest = student

    # Attach latest status
    highest["status"] = calculate_status(highest["score"])

    return highest


# ------------------------------------------
# Search Student by Name
# ------------------------------------------
def search_student(name):

    for student in students:

        if student["name"].lower() == name.lower():

            student["status"] = calculate_status(student["score"])

            return student

    return "Not Found"


# ------------------------------------------
# Bonus
# List Comprehension
# ------------------------------------------
def top_scorers():

    return [
        student["name"]
        for student in students
        if calculate_status(student["score"]) == "Distinction"
    ]


# ==========================================
# Main Program
# ==========================================

list_students()

print("\nUnique Subjects")
print(unique_subjects())

print("\nPass Cutoffs")
print(PASS_CUTOFFS)

add_student("Frank", "Python", 77)

list_students()

print(f"\nPython Average : {class_average('Python'):.2f}")
print(f"DSA Average    : {class_average('DSA'):.2f}")

print("\nTop Scorer")
print(top_scorer())

print("\nSearch Student")
print(search_student("Charlie"))

print("\nTop Scorers")
print(top_scorers())