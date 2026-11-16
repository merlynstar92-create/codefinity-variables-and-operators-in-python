# Number of classes and students per class
classes = 6  #num. of current classes
students = 45  #total num. of students in one class

# Calculate total number of students
total_students = classes*students

# Calculate total number of classes
total_classes = total_students//27

# Testing
print("Number of students:", total_students)
print("Number of groups:", total_classes)