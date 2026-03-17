
from copy import copy


student1 = {
    "name": "Manoj",
    "marks": [80, 85, 90]
}


student2 = student1.copy()


student2.get("marks").append(95)
# student2["marks"].append(95)

print(student1)
print(student2)