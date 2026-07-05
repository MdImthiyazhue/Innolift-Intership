import numpy as np

# Dictionary to store the step data
step_data = {}

# Read the file safely
try:
    with open("steps_log.txt", "r") as file:
        for line in file:
            day, steps = line.strip().split(":")
            step_data[day] = int(steps)

except FileNotFoundError:
    print("steps_log.txt not found.")
    exit()

days = list(step_data.keys())
steps = np.array(list(step_data.values()))

# Calculate statistics
average = steps.mean()
maximum = steps.max()
minimum = steps.min()

# Normalize activity score between 0 and 1
if maximum != minimum:
    activity = (steps - minimum) / (maximum - minimum)
else:
    activity = np.zeros(len(steps))

# Calculate goal achievement rate
def goal_rate(step_array):
    goal_days = np.sum(step_array >= 8000)
    return (goal_days / len(step_array)) * 100

# Find most and least active day
most_active = days[np.argmax(steps)]
least_active = days[np.argmin(steps)]

# Rank all days from highest to lowest
ranking = np.argsort(steps)[::-1]

print("===== FITTRACK WEEKLY REPORT =====")

for day, step, score in zip(days, steps, activity):
    print(f"{day:10} | Steps: {step:5} | Activity Score: {score:.2f}")

print("\n===== SUMMARY =====")

print(f"Average Steps : {average:.2f}")
print(f"Highest Steps : {maximum}")
print(f"Lowest Steps  : {minimum}")

print(f"\nGoal Achievement Rate : {goal_rate(steps):.2f}%")

print(f"Most Active Day  : {most_active}")
print(f"Least Active Day : {least_active}")

print("\n===== Ranking =====")

rank = 1
for index in ranking:
    print(f"{rank}. {days[index]} - {steps[index]} steps")
    rank += 1