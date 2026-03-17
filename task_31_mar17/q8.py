


from copy import deepcopy


student1 = {
    "name": "Manoj",
    "marks": [80, 85, 90],
    "details": {
        "age": 21,
        "course": "BCA"
    }
}

student2 = deepcopy(student1)

student2["marks"].append(95)
student2["details"]["age"] = 22

print(student1)
print(student2)
