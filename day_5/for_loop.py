# student_heights = input("Input a list of student heights ").split()
student_heights = [156, 178, 165, 171, 187]

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])



total_height = 0
total_student = 0
for height in student_heights:
    total_height += height
    total_student += 1
average_height = round(total_height / total_student)
print(average_height)



# student_heights = [180, 124, 165, 173, 189, 169, 146]
#
# all_summ = []
#
# for total_height in student_heights:
#     sum_heig = total_height
#     # all_summ.append(+total_height)
#     # all_summ[0] += total_height
#
#     print(all_summ)
