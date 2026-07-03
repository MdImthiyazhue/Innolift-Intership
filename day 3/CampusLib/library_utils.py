from datetime import datetime

# Find a book by title
def find_book(books, title):
    for book in books:
        if book["title"].lower() == title.lower():
            return book
    return None


# Write borrow/return activity to log file
def log_activity(action, title):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("borrow_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{time} | {action} | {title}\n")


# Bonus Report
def summarize_library(**stats):
    print("\n===== Library Summary =====")

    for key, value in stats.items():
        print(f"{key}: {value}")