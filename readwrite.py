# Python program to demonstrate file modes for reading and writing data

filename = "example.txt"

# 'w' mode: Write mode (overwrites the file if it exists, creates a new file if it doesn't)
with open(filename, 'w') as file:
    file.write("This is written in write mode.\n")
    file.write("All previous content will be erased.\n")
print("Data written in 'w' mode.")

# 'a' mode: Append mode (adds data to the end of the file without erasing existing content)
with open(filename, 'a') as file:
    file.write("This is written in append mode.\n")
print("Data appended in 'a' mode.")

# 'r' mode: Read mode (reads the file, throws an error if the file doesn't exist)
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("Data read in 'r' mode:")
        print(content)
except FileNotFoundError:
    print("File not found in 'r' mode.")

# 'r+' mode: Read and write mode (reads and writes, throws an error if the file doesn't exist)
try:
    with open(filename, 'r+') as file:
        file.write("This is written in r+ mode.\n")
        file.seek(0)  # Move the cursor to the beginning to read
        content = file.read()
        print("Data read in 'r+' mode:")
        print(content)
except FileNotFoundError:
    print("File not found in 'r+' mode.")

# 'w+' mode: Write and read mode (overwrites the file, creates a new file if it doesn't exist)
with open(filename, 'w+') as file:
    file.write("This is written in w+ mode.\n")
    file.seek(0)  # Move the cursor to the beginning to read
    content = file.read()
    print("Data read in 'w+' mode:")
    print(content)

# 'a+' mode: Append and read mode (appends data and allows reading)
with open(filename, 'a+') as file:
    file.write("This is written in a+ mode.\n")
    file.seek(0)  # Move the cursor to the beginning to read
    content = file.read()
    print("Data read in 'a+' mode:")
    print(content)

