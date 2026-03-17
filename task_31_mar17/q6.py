

# shallow copy

from copy import copy
lst1 = [
        ["vipin",29,"django"],
        ["edwin",23,"data science"],
        ["allan",22,"cloud computing"]

]

lst2 = copy(lst1)

lst2[0][0]="manoj"

print(lst1)
print(lst2)


#deep copy

from copy import deepcopy

lst1 = [
        ["vipin",29,"django"],
        ["edwin",23,"data science"],
        ["allan",22,"cloud computing"]

]

lst2 = deepcopy(lst1)

lst2[0][0]="manoj"

print(lst1)
print(lst2)

