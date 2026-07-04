# Day 4 - Task 5
# Digital Business Card using Dictionary

# Dictionary to store personal information
business_card = {
    "name": "Mohamed Imthiyas",
    "role": "AI & Data Science Student",
    "email": "mohamedimthiyas@example.com",
    "phone": "+91 9876543210",
    "linkedin": "linkedin.com/in/mohamedimthiyas"
}


# Function to display the business card
def display_card():
    print("\n===== DIGITAL BUSINESS CARD =====")
    print(f"Name      : {business_card['name']}")
    print(f"Role      : {business_card['role']}")
    print(f"Email     : {business_card['email']}")
    print(f"Phone     : {business_card['phone']}")
    print(f"LinkedIn  : {business_card['linkedin']}")


# Display the original card
display_card()

# Update the role
business_card["role"] = "Full Stack AI Developer Intern"

print("\nRole updated successfully!")

# Display the updated card
display_card()