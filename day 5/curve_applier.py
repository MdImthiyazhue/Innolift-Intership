import numpy as np

students = ["A", "B", "C", "D", "E", "F"]

raw_scores = np.array([72, 65, 80, 59, 91, 77])

curved_scores = raw_scores + 4

print("===== Exam Curve =====")

for s, r, c in zip(students, raw_scores, curved_scores):
    print(f"{s}: {r} -> {c}")

print()
print(f"Original Mean : {raw_scores.mean():.2f}")
print(f"Curved Mean   : {curved_scores.mean():.2f}")