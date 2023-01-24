student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for students in student_scores:
    if student_scores[students] <= 70:
        student_grades[students] = 'Grade = "Fail"'
    elif 70 < student_scores[students] <= 80:
        student_grades[students] = 'Grade = "Acceptable"'
    elif 80 < student_scores[students] <= 90:
        student_grades[students] = 'Grade = "Exceeds Expectations"'
    elif 90 < student_scores[students] <= 100:
        student_grades[students] = 'Grade = "Outstanding"'

# 🚨 Don't change the code below 👇
print(student_grades)
