# Initial values
is_student = False
is_smart = True
has_good_grades = False
has_extracurriculars = True

# Check if a student is eligible for scholarship with initial values
if is_student and is_smart and (has_good_grades or has_extracurriculars):
    print("You are eligible for the scholarship!")
else:
    print("You are not eligible for the scholarship.")

# Change the values of some variables
has_good_grades = True
has_extracurriculars = False

# Check if a student is eligible for scholarship with updated values
if is_student and is_smart and (has_good_grades or has_extracurriculars):
    print("You are eligible for the scholarship!")
else:
    print("You are not eligible for the scholarship.")
