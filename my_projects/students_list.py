student_list = {
    "English": ['Tim', 'Carl', 'Dean', 'Jane', 'Ann', 'Kate', 'Nick', 'Jenny'],
    "Maths": ['Jane', 'Mike', 'Ann', 'Kate', 'Nick', 'Jenny'],
    "Chemistry": ['Tim', 'Carl', 'Dean']
}

new_students_list = {key : len(value) for key, value in student_list.items()}
the_favorite_subject = max(new_students_list, key=new_students_list.get)
print(the_favorite_subject)

# fan, fach = 0, ""
#
# for subject, students in student_list.items():
#     if len(students) > fan:
#         fan = len(students)
#         fach = subject
# print(fach)


