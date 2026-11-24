def calculate_total(marks):
    return sum(marks)

def calculate_percentage(total):
    return (total / 500) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >=50:
        return "D"
    else:
        return "F"

student_name = input("Enter the student's name: ")
roll_number = input("Enter the roll number: ")

subjects = ["English", "Mathematics", "Computer Science", "Physics", "Chemistry"]
marks = []

for subject in subjects:
    while True:
        try:
            marks_input = float(input(f"Enter marks for {subject}: "))
            if marks_input >= 0 and marks_input <= 100:
                break
            else:
                print("Invalid marks. Please enter marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    marks.append(marks_input)

failed_subjects = [subject for subject, mark in zip(subjects, marks) if mark < 40]

if len(failed_subjects) > 0:
    status = "Needs Improvement - Failed in Subject(s)"
else:
    status = "Pass"