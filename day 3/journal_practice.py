from datetime import datetime


# Add a journal entry
def add_entry(text):
    with open("journal.txt", "a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time} - {text}\n")


# Display all journal entries
def show_entries():
    print("\n===== My Journal =====")

    with open("journal.txt", "r") as file:
        for line in file:
            print(line.strip())


# Add three entries
add_entry("Started learning Python functions.")
add_entry("Practiced file handling.")
add_entry("Completed the journal task.")

# Show all entries
show_entries()