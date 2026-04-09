# Program to find student with highest marks from dictionary

# Taking input manually (example dictionary)
marks = {"A": 80, "B": 95, "C": 78}

# Assume first student has highest marks
top_student = None
highest_marks = 0

# Loop through dictionary
for student in marks:
    
    # Check if current student's marks are greater
    if marks[student] > highest_marks:
        highest_marks = marks[student]   # Update highest marks
        top_student = student            # Update student name

# Display result
print("Student with highest marks =", top_student)