# Grade Checker Program

print("=== Grade Checker ===")
print("Type 'exit' to quit.\n")

# Keep running until the user types "exit"
while True:
    score = input("Enter score (0-100): ")

    # Exit condition
    if score.lower() == "exit":
        print("Closing Grade Checker")
        break

    # Convert input to integer
    score = int(score)

    # Determine the grade
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    elif score >= 50:
        grade = "C"
    else:
        grade = "Fail"

    # Display the result
    print(f"Score: {score}")
    print(f"Grade: {grade}\n")