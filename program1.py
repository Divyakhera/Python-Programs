#A school has following rules for grading system below 25-f  , 25 to 45-E  , 45 to 50-D , 50 to 60 - C ,  
#60 to 70 -B , 70 to 80 - A . write a python 
#function and program to ask user marks in 5 subjects calculate percentage for the corresponding  grade. 
def calculate_grade(mark):
    if mark < 25:
        return "F"
    elif mark < 45:
        return "E"
    elif mark < 50:
        return "D"
    elif mark < 60:
        return "C"
    elif mark < 70:
        return "B"
    else:
        return "A"

marks = []

for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))

total_marks = sum(marks)
percentage = (total_marks/500)*100
grade = calculate_grade(percentage)

print(f"Percentage: {percentage:.2f}")
print(f"Grade: {grade}")
