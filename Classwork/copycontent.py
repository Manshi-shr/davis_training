# write a program to copy the contents of one file into another file
# Program to copy contents of one file to another

# Open source file in read mode
source = open("list.py", "r")

# Open destination file in write mode
destination = open("destination.py", "w")

# Read content from source file
content = source.read()

# Write content into destination file
destination.write(content)

# Close both files
source.close()
destination.close()

print("File copied successfully!")