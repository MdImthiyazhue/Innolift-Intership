# Demo 5 - File I/O

# Write to a file
with open("notes.txt", "w") as file:
    file.write("Hello, Python!\n")

# Append to the same file
with open("notes.txt", "a") as file:
    file.write("Learning File Handling.\n")

# Read and display the file
with open("notes.txt", "r") as file:
    print(file.read())