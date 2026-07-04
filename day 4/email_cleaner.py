# Day 4 - Task 6
# Duplicate Email Cleaner using Set

# Original email list with duplicates
email_list = [
    "alice@gmail.com",
    "bob@gmail.com",
    "charlie@gmail.com",
    "alice@gmail.com",
    "david@gmail.com",
    "eve@gmail.com",
    "bob@gmail.com",
    "frank@gmail.com"
]

print("===== ORIGINAL EMAIL LIST =====")
for email in email_list:
    print(email)

# Convert list to set to remove duplicates
unique_emails = set(email_list)

# Calculate duplicate count
duplicates_removed = len(email_list) - len(unique_emails)

print("\n===== UNIQUE EMAILS =====")
for email in unique_emails:
    print(email)

print(f"\nOriginal Email Count : {len(email_list)}")
print(f"Unique Email Count   : {len(unique_emails)}")
print(f"Duplicates Removed   : {duplicates_removed}")