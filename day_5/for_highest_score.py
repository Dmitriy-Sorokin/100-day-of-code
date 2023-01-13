# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max_score = 0
for sc in student_scores:
    if max_score <= sc:
        max_score = sc
print(f"The highest score in the class is: {max_score}")

