


from copy import deepcopy


student1 = {

    "name": "Manoj",
    "marks": {"math": 80, "science": 85},
    "subjects": ["Math", "Science", "English"]
}


student2= deepcopy(student1)


student2["marks"]["math"] = 95
student2["subjects"].append("History")


print(student1)
print(student2)