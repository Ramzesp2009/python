import statistics

universities = [['California Institute of Technology', 2175, 37704],
                ['Harvers', 19627, 39849],
                ['Massachusetts Institute of Technology', 10566, 40732],
                ['Princeton', 7802, 37000],
                ['Rice', 5879, 35551],
                ['Stanfors', 19535, 40569],
                ['Yale', 11701, 40500]
                ]


def enrollment_stats(uni):
    students = [i[1] for i in uni]
    tuitions = [i[2] for i in uni]

    total_students = sum(students)
    total_tuition = sum(tuitions)

    student_mean = statistics.mean(students)
    student_median = statistics.median(students)

    tuition_mean = statistics.mean(tuitions)
    tuition_mediean = statistics.median(tuitions)

    return  total_students, total_tuition, student_mean, student_median, tuition_mean, tuition_mediean

stats = enrollment_stats(universities)

print('*' * 30)
print(f'Total students: {stats[0]:,}')
print(f'Total tuition: $ {stats[1]:,}')
print()

print(f'Student_mean: {stats[2]:,.2F}')
print(f'Student_median: {stats[3]:,}')
print()

print(f'Tuition_mean: $ {stats[4]:,.2F}')
print(f'Tuition_mediean: $ {stats[5]:,}')

print('*' * 30)