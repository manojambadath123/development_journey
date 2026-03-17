

# data = [(1, 5), (3, 2), (4, 8), (2, 1)]

# sorted_data = sorted(data, key=lambda x: x[1])

# print(sorted_data)


# data = [(1, 5), (3, 2), (4, 8), (2, 1)]

# data.sort(key=lambda x: x[1])

# print(data)



students = [

    ("hari",145),
    ("vipin",135),
    ("john",125),
    ("smith",175),
    ("doe",165),
]


# def get_second_element(tp):

#     return tp[1]

# lambda tp : tp[1]

students.sort(key = lambda tp :tp[1],reverse=True)

print(students)

# print(sum(students,key = lambda tp:tp[1]))

print(max(students,key=lambda tp:tp[1]))

print(sorted(students,key = lambda tp:tp[1],reverse=True))
